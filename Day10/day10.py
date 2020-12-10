
from typing import List
from collections import Counter

def calc_num_combos(n_gaps,start_gap):
    """Return number of combinations given a run starting and ending with diffs of 3, with n_gaps 1s in between."""
    if start_gap>3:
        return 0
    if n_gaps == 1:
        return 1
    return calc_num_combos(n_gaps-1,start_gap+1)+calc_num_combos(n_gaps-1,1)
    
def calc_num_variations(diffs: List[int]):
    """Total number of combinations, calculated by multiplying the # combinations for each run of 1s"""
    s = ''.join(str(d) for d in diffs)
    
    runs = []
    while s.find('1')!=-1:
        s = s[s.find('1'):]
        runs += [s.find('3')]
        s = s[runs[-1]:]
    
    n_combos = 1
    for l in runs:
        n_combos *= calc_num_combos(l,1)
    return n_combos

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        numbers = [int(n.rstrip('\n')) for n in f.readlines()]
        
    sorted_numbers = sorted(numbers)
    sorted_numbers = [0]+sorted_numbers+[sorted_numbers[-1]+3]
    diffs = []
    for i in range(0,len(sorted_numbers)-1):
        diffs += [sorted_numbers[i+1]-sorted_numbers[i]]
        
    c = Counter(diffs)
    print('Product of #1s and #3s is: {0}'.format(c[1]*c[3]))
    print('Number of variations is {0}'.format(calc_num_variations(diffs)))
    
    