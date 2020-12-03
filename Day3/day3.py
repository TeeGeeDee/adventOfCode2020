
from typing import List
from math import prod


def traverse(down: int,right: int,terrain: List[str]):
    """ Counts number of trees passed when traversing terrane with given step sizes
    
    Parameters
    ----------
    down: int
        number of steps to take down each iteration
    right: int
        number of steps to take right each iteration
    terrain: list of str
        representing terrain. '#' represents tree

    Returns
    -------
    number of trees the traveral goes through

    """
    y_pos,x_pos,num_trees = down,right,0
    while y_pos<=len(terrain)-1:
        num_trees += terrain[y_pos][x_pos % len(terrain[y_pos])]=='#'
        y_pos += down
        x_pos += right
    return num_trees


if __name__ == "__main__":

    with open("data.txt", "r") as f:
        slope = [x.rstrip('\n') for x in f.readlines()]
    params = [(1,1),(1,3),(1,5),(1,7),(2,1)]

    
    print('Number of trees his is {0}'.format(traverse(1,3,slope)))
    print('Product of trees seen is {0}'.format(prod([traverse(*p,slope) for p in params])))

        