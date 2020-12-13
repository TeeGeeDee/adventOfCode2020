
from typing import List,Callable
from copy import deepcopy

def update_seats(seats: List[List[str]],seat_counter: Callable,thresh: int):
    to_switch = []
    switcher = {'L':'#','#':'L'}
    for row in range(0,len(seats)):
        for col in range(0,len(seats[0])):
            if seats[row][col]=='L' and seat_counter(seats,row,col)==0:
                to_switch += [(row,col)]
            elif seats[row][col]=='#' and seat_counter(seats,row,col)>=thresh:
                to_switch += [(row,col)]
    if len(to_switch)==0:
        return seats
    else:
        for i in range(0,len(to_switch)):
            seats[to_switch[i][0]][to_switch[i][1]] = switcher[seats[to_switch[i][0]][to_switch[i][1]]]
        return update_seats(seats,seat_counter,thresh)

def num_adj_taken(seats: List[List[str]],r: int,c: int):
    num_taken = 0
    for r_mod in (-1,0,1):
        for c_mod in (-1,0,1):
            if (0<=r+r_mod<=len(seats)-1) and (0<=c+c_mod<=len(seats[0])-1) and (not (c_mod==0 and r_mod==0)):
                num_taken += int(seats[r+r_mod][c+c_mod]=='#')
    return num_taken

def calc_num_taken(seats: List[List[str]],r: int,c: int):
    # this time implement with single pass through in each direction across the whole dataset, counting how much each seat can see?
    num_taken = 0
    for r_mod in (-1,0,1):
        for c_mod in (-1,0,1):
            view_seat = (r+r_mod,c+c_mod)
            while (0<=view_seat[0]<=len(seats)-1) and (0<=view_seat[1]<=len(seats[0])-1) \
                and (view_seat!=(r,c)):
                    state = seats[view_seat[0]][view_seat[1]]
                    if state!='.':
                        num_taken += state=='#'
                        break
                    else:
                        view_seat = (view_seat[0]+r_mod,view_seat[1]+c_mod)
    return num_taken

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        seats = [list(c.rstrip('\n')) for c in f.readlines()]

    seats_copy = deepcopy(seats)
    final_seats1 = update_seats(seats,num_adj_taken,4)
    final_seats2 = update_seats(seats_copy,calc_num_taken,5)
    print('{0} seats end up occupied for part 1.'.format(sum(s=='#' for r in final_seats1 for s in r)))
    print('{0} seats end up occupied for part 2.'.format(sum(s=='#' for r in final_seats2 for s in r)))

    