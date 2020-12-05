
from typing import List
from collections import Counter

def parse_ticket(ticket: str):
    """Turns str representation of ticket (of the form 8 F/B followed by 3 R/L)
    to tuple of row and column numbers
    

    Parameters
    ----------
    ticket : str
        binary string representation of seat e.g. 'FBFFBFFBRLR'

    Returns
    -------
    row : int
        seat row number
    col : int
        seat column number

    """
    fb,rl = ticket[0:7],ticket[7:]
    row = int(fb.replace('B','1').replace('F','0'),2)
    col = int(rl.replace('R','1').replace('L','0'),2)
    return row, col

def get_seat_num(row,col):
    return 8*row+col

def find_my_seat(tickets_full: List[tuple]):
    """Given list of row,column pairs, finds the missing seat number, given
    that we know the missing seat has 8 people in both the row behind and in front
    

    Parameters
    ----------
    tickets_full : List[tuple]
        List of taken seats, represented by (row,column) tuples

    Returns
    -------
    my_row : int
        remaining seat row number
    my_col : int
        remaining seat column number

    """
    r_counts = Counter([t[0] for t in tickets_full]).most_common()
    full_rows = [r[0] for r in r_counts if r[1]==8]
    front_row, back_row = min(full_rows), max(full_rows)
    my_row = [rc[0] for rc in r_counts if (rc[1]==7 and front_row<rc[0]<back_row)][0]
    my_row_taken_cols = [t[1] for t in tickets_full if t[0]==my_row]
    my_col = [c for c in range(0,8) if c not in my_row_taken_cols][0]
    return my_row, my_col


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        tickets = [r.rstrip('\n') for r in f.readlines()]
    
    print('The maximum seat number is {0}'.format(max([get_seat_num(*parse_ticket(t)) for t in tickets])))
    print('My seat number is {0}'.format(get_seat_num(*find_my_seat([parse_ticket(t) for t in tickets]))))
