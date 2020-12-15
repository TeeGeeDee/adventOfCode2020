
from typing import Tuple

DATA = (1,0,18,10,19,6)
TESTS = {(0,3,6):436,(1,3,2):1,(2,1,3):10,(1,2,3):27,(2,3,1):78,(3,2,1):438,(3,1,2):1836}
TESTS2 = {(0,3,6):175594,(1,3,2):2578,(2,1,3):3544142,(1,2,3):261214,(2,3,1):6895259, \
          (3,2,1):18,(3,1,2):362}


def get_nth_in_seq(start: Tuple[int],n: int):
    last_time_seen = {}
    current_num = start[0]
    for ii in range(0,n):
        if ii<len(start):
            current_num = start[ii]
            next_num = start[ii]
            if ii<len(start)-1:
                last_time_seen[current_num] = ii
        else:
            if current_num in last_time_seen:
                next_num = ii-1-last_time_seen[current_num]
            else:
                next_num = 0
            last_time_seen[current_num] = ii-1
            current_num = next_num
    return next_num


if __name__ == '__main__':

    for e in TESTS:
        print('My answer = {0} vs given answer {1}'.format(get_nth_in_seq(e, 2020),TESTS[e]))
    
    print('Part 1 2020th number called is {0}'.format(get_nth_in_seq(DATA, 2020)))
    
    for e in TESTS2:
        print('My answer = {0} vs given answer {1}'.format(get_nth_in_seq(e, 30000000),TESTS2[e]))
    
    print('Part 2 30000000 number called is {0}'.format(get_nth_in_seq(DATA, 30000000)))
