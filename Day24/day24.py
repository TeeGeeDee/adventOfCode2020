
from typing import List
from collections import Counter

NEIGHBOURS = ((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))

def flip_tiles(data: List[str]):
    black_tiles = set()
    for row in data:
        moves = Counter()
        for ix in range(len(row)):
            if row[ix] in ('n','s'):
                continue
            elif ix>0 and row[ix-1] in ('n','s'):
                direction = row[ix-1:ix+1]
            else:
                direction = row[ix]
            moves[direction] += 1
        canonical_form = (2*moves['e']+moves['ne']+moves['se']-(2*moves['w']+moves['nw']+moves['sw']),
                                                                  moves['ne']+moves['nw']-(moves['se']+moves['sw']))
        if canonical_form in black_tiles:
            black_tiles.remove(canonical_form)
        else:
            black_tiles.add(canonical_form)
    return black_tiles

def day_update(black_tiles: set):
    flip_to_white = set()
    for tile in black_tiles:
        num_black_neighbours = sum((tile[0]+mv[0],tile[1]+mv[1]) in black_tiles for mv in NEIGHBOURS)
        if num_black_neighbours == 0 or num_black_neighbours > 2:
            flip_to_white.add(tile)
    flip_to_black = set()
    all_neighbours = tuple((tile[0]+mv[0],tile[1]+mv[1]) for mv in NEIGHBOURS for tile in black_tiles)
    for tile in all_neighbours:
        if sum((tile[0]+mv[0],tile[1]+mv[1]) in black_tiles for mv in NEIGHBOURS) == 2:
            flip_to_black.add(tile)
    black_tiles.difference_update(flip_to_white)
    black_tiles.update(flip_to_black)
    return black_tiles


if  __name__ == '__main__':
    
    with open('data.txt') as f:
        data = [r.rstrip('\n') for r in f]
    
    black_tiles = flip_tiles(data)
    print('Part 1 ends up with {0} black tiles'.format(len(black_tiles)))
    
    for ii in range(100):
        day_update(black_tiles)
    print('Part 2 ends up with {0} black tiles'.format(len(black_tiles)))
        