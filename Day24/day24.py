
from typing import List
from collections import Counter

def canonical_form(mv: Counter):
    return (2*mv['e']+mv['ne']+mv['se']-2*mv['w']-mv['nw']-mv['sw'], mv['ne']+mv['nw']-mv['se']-mv['sw'])

def neighbours(tile):
    return [(tile[0]+mv[0],tile[1]+mv[1]) for mv in ((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))]

def flip_tiles(flip_list: List[str]):
    black_tiles = set()
    for row in flip_list:
        moves = Counter()
        for ix in range(len(row)):
            if row[ix] in ('n','s'):
                continue
            elif ix>0 and row[ix-1] in ('n','s'):
                direction = row[ix-1:ix+1]
            else:
                direction = row[ix]
            moves[direction] += 1
        tile = canonical_form(moves)

        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)
    return black_tiles

def day_update(black_tiles: set):
    flip_to_white = [tile for tile in black_tiles if len(black_tiles.intersection(neighbours(tile))) not in (1,2)]
    white_tiles = set(tile for bt in black_tiles for tile in neighbours(bt) if tile not in black_tiles)
    flip_to_black = [tile for tile in white_tiles if len(black_tiles.intersection(neighbours(tile))) == 2]
    black_tiles.difference_update(flip_to_white)
    black_tiles.update(flip_to_black)
    return black_tiles

if  __name__ == '__main__':
    
    with open('data.txt') as f:
        flip_list = [r.rstrip('\n') for r in f]
    
    black_tiles = flip_tiles(flip_list)
    print('Part 1 has {0} black tiles'.format(len(black_tiles)))
    
    for _ in range(100):
        day_update(black_tiles)
    print('Part 2 has {0} black tiles'.format(len(black_tiles)))
        