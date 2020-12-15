
from typing import Tuple

DATA = (1,0,18,10,19,6)
TESTS = {(0,3,6):436,(1,3,2):1,(2,1,3):10,(1,2,3):27,(2,3,1):78,(3,2,1):438,(3,1,2):1836}
TESTS2 = {(0,3,6):175594,(1,3,2):2578,(2,1,3):3544142,(1,2,3):261214,(2,3,1):6895259, \
          (3,2,1):18,(3,1,2):362}


def get_nth_in_seq(start: Tuple[int],n: int):
    last_time_seen = {start[i]:i for i in range(0,len(start)-1)}
    current_num = start[-1]
    for ix_prev in range(len(start)-1,n-1):
        if current_num in last_time_seen:
            next_num = ix_prev-last_time_seen[current_num]
        else:
            next_num = 0
        last_time_seen[current_num] = ix_prev
        current_num = next_num
    return next_num


if __name__ == '__main__':

    for e in TESTS:
        print('My answer = {0} vs given answer {1}'.format(get_nth_in_seq(e, 2020),TESTS[e]))
    
    print('Part 1 2020th number called is {0}'.format(get_nth_in_seq(DATA, 2020)))
    
    for e in TESTS2:
        print('My answer = {0} vs given answer {1}'.format(get_nth_in_seq(e, 30000000),TESTS2[e]))
    
    print('Part 2 30000000 number called is {0}'.format(get_nth_in_seq(DATA, 30000000)))
