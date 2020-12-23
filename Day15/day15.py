
from typing import Tuple

DATA = (1,0,18,10,19,6)


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

    print('Part 1 2020th number called is {0}'.format(get_nth_in_seq(DATA, 2020)))
    
    print('Part 2 30000000 number called is {0}'.format(get_nth_in_seq(DATA, 30000000)))
