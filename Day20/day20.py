
from typing import List,Tuple
from enum import Enum

MONSTER = ('                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ')

class Modifier(Enum):
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
    
    def get_side_of_modified_image(self,raw_image: List[str],side):
        """Return side of modified image (quicker than making image).
        
        Read left to right, or top down.
        0=top,1=right,2=bottom,3=left
        
        """
        side = 'urdl'.index(side)
        if self.is_flip():
            side = 3-side
        start = side
        side = (side - self.n_rotation()) % 4
        read_order_reverse = ((start//2)!=(side//2))

        if side == 0:
            side = raw_image[0]
        elif side == 2:
            side = raw_image[-1]
        elif side == 1:
            side = ''.join([x[-1] for x in raw_image])
        elif side == 3:
            side = ''.join([x[0] for x in raw_image])
        if read_order_reverse:
            side = side[::-1]
        return side
    
    def modify(self,raw_image: List[str]):
        n = len(raw_image)
        if self.n_rotation() == 0:
            start = [0,0]
            move = (0,1)
            newline = (1,0)
        elif self.n_rotation() == 1:
            start = [n-1,0]
            move = (-1,0)
            newline = (0,1)
        elif self.n_rotation() == 2:
            start = [n-1,n-1]
            move = (0,-1)
            newline = (-1,0)
        else:
            start = [0,n-1]
            move = (1,0)
            newline = (0,-1)
        if self.is_flip():
            move,newline = newline,move
        out = []
        while 0<=start[0]<n and 0<=start[1]<n:
            out.append('')
            xy = start.copy()
            while 0<=xy[0]<n and 0<=xy[1]<n:
                out[-1] += raw_image[xy[0]][xy[1]]
                xy[0] += move[0]
                xy[1] += move[1]
            start[0] += newline[0]
            start[1] += newline[1]
        return out
    
class TileCache:
    def __init__(self,tile_input: Tuple[str]):
        tiles = {}
        ii = 0
        while ii<len(tile_input):
            if tile_input[ii].startswith('Tile '):
                jj = 0
                while ii+jj <len(tile_input) and tile_input[jj]!='':
                    jj += 1
                tiles[tile_input[ii][5:9]] = tuple(tile_input[ii+1:ii+jj])
                ii += jj
            else:
                ii += 1
                continue
        self.tiles = tiles
        self.n = int(len(tiles)**0.5)
        self.compile_matches()
    
    def compile_matches(self):
        """Produce dict with key for each (ID, modification and r/d side), with value the set of matching ID,modification pairs"""
        all_sides = {(ID,mod,side): mod.get_side_of_modified_image(self.tiles[ID],side)
                     for ID in self.tiles
                     for mod in Modifier
                     for side in 'urdl'}
        self.match_map = {(ID,mod):{'r':set((ID2,mod2)
                                      for ID2 in self.tiles
                                      for mod2 in Modifier
                                      if all_sides[(ID,mod,'r')]==all_sides[(ID2,mod2,'l')]),
                                   'd':set((ID2,mod2)
                                      for ID2 in self.tiles
                                      for mod2 in Modifier
                                      if all_sides[(ID,mod,'d')]==all_sides[(ID2,mod2,'u')])
                                   }
                         for ID in self.tiles
                         for mod in Modifier}

    
    def stitch_tiles(self,so_far: Tuple[Tuple]):
        """Recursive greedy function for composing tiles that match on right/bottom of existing"""
        matches = set(t for t in self.match_map if t[0] not in set(x[0] for x in so_far))
        if len(so_far) > self.n-1:
            matches.intersection_update(self.match_map[so_far[-self.n]]['d'])
        if len(so_far) % self.n > 0:
            matches.intersection_update(self.match_map[so_far[-1]]['r'])
        out = None
        for next_tile in matches:
            next_try = so_far+(next_tile,)
            if len(next_try)==self.n**2:
                return next_try
            out = self.stitch_tiles(next_try)
            if out is not None:
                break
        return out
    
    def print_arrangement(self,arrangement: Tuple[Tuple]):
        composite = []
        for ix in range(len(arrangement)):
            image = arrangement[ix][1].modify(self.tiles[arrangement[ix][0]])
            image = [r[1:-1] for r in image[1:-1]]
            if ix % self.n == 0:
                composite.append(image)
            else:
                for row in range(len(composite[-1])):
                    composite[-1][row] += image[row]
        return tuple(item for sublist in composite for item in sublist)
        

def find_monsters(image: List[str]):
    """Search for monster in image, in panel starting (x,y).  Return coordinates if there"""
    monster_pixels = set()
    for x in range(len(image)+1-len(MONSTER)):
        for y in range(len(image[0])+1-len(MONSTER[0])):
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
            if is_ok:
                monster_pixels.update(coords_match)
    return monster_pixels


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        data = tuple(c.rstrip('\n') for c in f.readlines())
    
    tile_cache = TileCache(data)
    arrangement = tile_cache.stitch_tiles(())
    
    print('Part 1 answer is {0}'.format(int(arrangement[0][0])*int(arrangement[tile_cache.n-1][0])*
                                        int(arrangement[tile_cache.n**2-tile_cache.n][0])*int(arrangement[tile_cache.n**2-1][0])))
    
    composite = tile_cache.print_arrangement(arrangement)
    for mod in Modifier:
        image = mod.modify(composite)
        monster_pixels = find_monsters(image)
        if len(monster_pixels)>0:
            break
        
    print('There are {0} \'#\' that are not part of a monster'.format(sum(row.count('#') for row in image) - len(monster_pixels)))
                
    