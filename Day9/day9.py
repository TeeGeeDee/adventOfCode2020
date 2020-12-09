
from typing import List

def contains_summing_pair(x: List[int],total: int):
    """Return bool 'is there are a pair of ints in x that sum to total?'."""
    x_set = set(x)
    if x.count(total/2)==1: # special case that breaks "is sum_constraint-me in set" below logic
        x_set.remove(total/2)
    i = 0
    while i<len(x) and total-x[i] not in x_set:
        i += 1
    return i<len(x)

def find_first_bad_num(numbers: List[int]):
    """Return first number that can't be written as the sum of 2 of the previous 25."""
    i = 25
    while contains_summing_pair(numbers[i-25:i], numbers[i]):
        i += 1
    return numbers[i]

def get_encryption_weakness(numbers: List[int],total: int):
    """Return sum of max and min of interval that sums to total."""
    found = False
    i = 0
    while not found:
        i += 1
        j = i
        s = 0
        while s <total:
            s += numbers[j]
            j += 1
            found = s == total
    return min(numbers[i:j])+max(numbers[i:j])

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        numbers = [int(c.rstrip('\n')) for c in f.readlines()]

    bad_num = find_first_bad_num(numbers)
    print('First bad number is {0}'.format(bad_num))  
    print('sum of max and min in range is {0}'.format(get_encryption_weakness(numbers,bad_num)))
    
    