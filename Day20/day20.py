
from typing import List
from enum import Enum

MONSTER = ('                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ')

class Mod(Enum):
    NOTHING = 0
    ROT90 = 1
    ROT180 = 2
    ROT270 = 3
    FLIPPED = 4
    ROT90FLIPPED = 5
    ROT180FLIPPED = 6
    ROT270FLIPPED = 7
    
    def is_flip(self):
        return self.value>3
    
    def n_rotation(self):
        return self.value % 4


class Tile:
    def __init__(self,raw_image: List[str],mod: Mod):
        self.raw_image = raw_image
        self.mod = mod
        return

    def get_side(self,ix_side):
        """Return side of modified image.
        
        Read left to right, or top down.
        0=top,1=right,2=bottom,3=left
        
        """
        ix_start = ix_side
        ix_side = (ix_side - self.mod.n_rotation()) % 4
        read_order_change = ((ix_start//2)!=(ix_side//2))
        if self.mod.is_flip():
            ix_side = 3-ix_side

        if ix_side == 0:
            side = self.raw_image[0]
        elif ix_side == 2:
            side = self.raw_image[-1]
        elif ix_side == 1:
            side = ''.join([x[-1] for x in self.raw_image])
        elif ix_side == 3:
            side = ''.join([x[0] for x in self.raw_image])
        if read_order_change:
            side = side[::-1]
        return side

    def modified_image(self):
        n = len(self.raw_image)
        if self.mod.value % 4 == 0:
            start = [0,0]
            move = (0,1)
            newline = (1,0)
        elif self.mod.value % 4 == 1:
            start = [n-1,0]
            move = (-1,0)
            newline = (0,1)
        elif self.mod.value % 4 == 2:
            start = [n-1,n-1]
            move = (0,-1)
            newline = (-1,0)
        else:
            start = [0,n-1]
            move = (1,0)
            newline = (0,-1)
        if self.mod.is_flip(): 
            move,newline = newline,move
        out = []
        while 0<=start[0]<n and 0<=start[1]<n:
            out.append('')
            xy = start.copy()
            while 0<=xy[0]<n and 0<=xy[1]<n:
                out[-1] += self.raw_image[xy[0]][xy[1]]
                xy[0] += move[0]
                xy[1] += move[1]
            start[0] += newline[0]
            start[1] += newline[1]
        return out
    
def strip_outer_layer(image):
    return [r[1:-1] for r in image[1:-1]]

def monster_match(image,x,y):
    is_ok = True
    ii,jj = 0,0
    coords_match = set()
    while is_ok and ii<len(MONSTER) and jj<len(MONSTER[0]):
        if MONSTER[ii][jj] == '#':
            is_ok &= image[x+ii][y+jj] == '#'
            coords_match.add((x+ii,y+jj))
        jj += 1
        if jj ==len(MONSTER[0]):
            jj = 0
            ii += 1
    return is_ok,coords_match

def match_map_right_down(tiles: dict):
    match_map = {}
    for ID in tiles.keys():
        for mod in Mod:
            tile1 = Tile(tiles[ID],mod)
            match_map[(ID,mod,'r')] = set()
            match_map[(ID,mod,'d')] = set()
            for ID2 in set(tiles.keys()).difference([ID]):
                for mod2 in Mod:
                    tile2 = Tile(tiles[ID2],mod2)
                    if tile1.get_side(1) == tile2.get_side(3):
                        match_map[(ID,mod,'r')].add((ID2,mod2))
                    if tile1.get_side(2) == tile2.get_side(0):
                        match_map[(ID,mod,'d')].add((ID2,mod2))
    return match_map


def greedy_compose(so_far,match_map,n):
    if len(so_far)>(n-1) and len(so_far) % n > 0:
        poss = match_map[so_far[-n]+tuple(['d'])].intersection(match_map[so_far[-1]+tuple(['r'])])
    elif len(so_far) % n > 0:
        poss = match_map[so_far[-1]+tuple(['r'])]
    elif len(so_far)>(n-1):
        poss = match_map[so_far[-n]+tuple(['d'])]
    poss = [p for p in poss if p[0] not in set(x[0] for x in so_far)]
    out = None
    for next_tile in poss:
        if len(so_far)==n**2-1:
            return so_far+tuple([next_tile])
        out = greedy_compose(so_far+tuple([next_tile]),match_map,n)
        if out is not None:
            break
    return out


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        data = [c.rstrip('\n') for c in f.readlines()]
        
    tiles = {}
    ii = 0
    while ii<len(data):
        if data[ii].startswith('Tile '):
            jj = 0
            while ii+jj <len(data) and data[jj]!='':
                jj +=1
            tiles[data[ii][5:9]] = tuple(data[ii+1:ii+jj])
            ii += jj
        else:
            ii += 1
            continue
    
    n = int(len(tiles)**0.5)
    compat_cache = match_map_right_down(tiles)
    for kk in set(x[0:2] for x in compat_cache):
        tile_orientation = greedy_compose(tuple([kk[0:2]]),compat_cache,n)
        if tile_orientation is not None:
            break
    print('Part 1 answer is {0}'.format(int(tile_orientation[0][0])*int(tile_orientation[n-1][0])*int(tile_orientation[n**2-n][0])*int(tile_orientation[n**2-1][0])))
    
    composite = []
    for ix in range(len(tile_orientation)):
        tile = Tile(tiles[tile_orientation[ix][0]],tile_orientation[ix][1])
        output = strip_outer_layer(tile.modified_image())
        if ix % n == 0:
            composite.append(output)
        else:
            for row in range(len(composite[-1])):
                composite[-1][row] += output[row]

    composite = tuple(item for sublist in composite for item in sublist)
    
    sightings = 0
    matches = set()
    for mod in Mod:
        tile = Tile(composite,mod)
        image = tile.modified_image()
        for ii in range(len(image)+1-len(MONSTER)):
            for jj in range(len(image[0])+1-len(MONSTER[0])):
                is_monster,monster_coords = monster_match(image, ii, jj)
                sightings += is_monster
                if is_monster:
                    matches.update(monster_coords)
        if sightings>0:
            break
    
    num_hash = sum(ch=='#' for row in image for ch in row) - len(matches)
    
    print('There are {0} \'#\' that are not part of a monster'.format(sum(row.count('#') for row in image) - len(matches)))
                
    