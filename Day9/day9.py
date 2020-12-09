
from typing import List

def find_pair_with_sum(x: List[int],total: int):
    x_set = set(x)
    if x.count(total/2)==1: # special case that breaks "is sum_constraint-me in set" below logic
        x_set.remove(total/2)
    found = False
    i = 0
    while not found and i<len(x):
        found = total-x[i] in x_set
        i += 1
    return found

def find_first_bad_num(numbers: List[int]):
    for i in range(25,len(numbers)+1):
        found = find_pair_with_sum(numbers[i-25:i], numbers[i])
        if not found:
            break
    return i

def find_max_min_sum_in_containing_range(numbers: List[int],end_index: int):
    found = False
    i = 0
    while not found and i < end_index:
        i += 1
        s = 0
        j=i
        while s <numbers[end_index]:
            s += numbers[j]
            j += 1
            found = s == numbers[end_index]
    return min(numbers[i:j])+max(numbers[i:j])

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        numbers = [int(c.rstrip('\n')) for c in f.readlines()]

    end_ind = find_first_bad_num(numbers)
    print('First bad number is {0}'.format(numbers[end_ind]))  
    print('sum of max and min in range is {0}'.format(find_max_min_sum_in_containing_range(numbers,end_ind)))
    
        
    
    