
from enum import Enum

FLIPMAP = {0:3,3:0,2:1,1:2}

class Mod(Enum):
    NOTHING = 0
    ROT90 = 1
    ROT180 = 2
    ROT270 = 3
    FLIPPED = 4
    ROT90FLIPPED = 5
    ROT180FLIPPED = 6
    ROT270FLIPPED = 7

class Tile:
    def __init__(self,ID: str,mod,data: dict):
        self.ID = ID
        if type(mod)==str:
            mod = Mod[mod.upper()]
        elif type(mod)==int:
            mod = Mod(mod)
        self.mod = mod
        self.tile_data = data[ID]
        return

    def get_side(self,ix_side):
        """Read left to right, or top down"""
        ix_start = ix_side
        n_rot = self.mod.value % 4
        ix_side = (ix_side - n_rot) % 4
        if self.mod.value>3:
            ix_side = FLIPMAP[ix_side]
        flip = self.mod.value//4
        flip = bool((flip + (((ix_start//2)!=(ix_side//2)))) % 2)

        if ix_side == 0:
            side = self.tile_data[0]
        elif ix_side == 2:
            side = self.tile_data[-1]
        elif ix_side == 1:
            side = ''.join([x[-1] for x in self.tile_data])
        elif ix_side == 3:
            side = ''.join([x[0] for x in self.tile_data])
        if flip:
            side = side[::-1]
        return side
    

def compatabile_opts(tiles):
    compatability_cache = {}
    for ID in tiles.keys():
        for mod in Mod:
            tile1 = Tile(ID,mod,tiles)
            compatability_cache[(ID,mod,'r')] = set()
            compatability_cache[(ID,mod,'d')] = set()
            for ID2 in set(tiles.keys()).difference([ID]):
                for mod2 in Mod:
                    tile2 = Tile(ID2,mod2,tiles)
                    if tile1.get_side(1) == tile2.get_side(3):
                        compatability_cache[(ID,mod,'r')].add((ID2,mod2))
                    if tile1.get_side(2) == tile2.get_side(0):
                        compatability_cache[(ID,mod,'d')].add((ID2,mod2))
    return compatability_cache


def fill_next(so_far,compat_map,n):
    if len(so_far)>(n-1) and len(so_far) % n > 0:
        poss = compat_map[so_far[-n]+tuple(['d'])].intersection(compat_map[so_far[-1]+tuple(['r'])])
    elif len(so_far) % n > 0:
        poss = compat_map[so_far[-1]+tuple(['r'])]
    elif len(so_far)>(n-1):
        poss = compat_map[so_far[-n]+tuple(['d'])]
    poss = [p for p in poss if p[0] not in set(x[0] for x in so_far)]
    out = None
    for next_tile in poss:
        if len(so_far)==n**2-1:
            return so_far+tuple([next_tile])
        out = fill_next(so_far+tuple([next_tile]),compat_map,n)
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
            tiles[data[ii][5:9]] = data[ii+1:ii+jj]
            ii += jj
        else:
            ii += 1
            continue
    
    n = int(len(tiles)**0.5)
    compat_cache = compatabile_opts(tiles)
    for kk in set(x[0:2] for x in compat_cache):
        out = fill_next(tuple([kk[0:2]]),compat_cache,n)
        if out is not None:
            break
    print('Part 1 answer is {0}'.format(int(out[0][0])*int(out[n-1][0])*int(out[n**2-n][0])*int(out[n**2-1][0])))
        
    