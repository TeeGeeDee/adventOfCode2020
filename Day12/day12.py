
from typing import List

COMPASS = ('N','E','S','W')

class Ship:
    def __init__(self,rule):
        self.facing = 'E'
        self.pos = [0,0]
        self.waypoint = [10,1]
        self.rule = rule
        
    def move(self,instruction: str):
        action,value = instruction[0],int(instruction[1:])
        return getattr(self,'move'+str(self.rule))(action,value)
    
    def move1(self,action: str,value: int):
        if action == 'F':
            action = self.facing

        if action in ('L','S','W'):
            value = -1*value

        if action in COMPASS:
            self.pos[(1+COMPASS.index(action)) % 2] += value
        else:
            ix_dir = COMPASS.index(self.facing)
            self.facing = COMPASS[(ix_dir + value//90) % len(COMPASS)]
        return

    def move2(self,action: str,value: int):
        if action in ('L','S','W'):
            value = -1*value

        if action in COMPASS:
            if action in ('N','S'):
                self.waypoint[(1+COMPASS.index(action)) % 2] += value
        elif action =='F':
            self.pos = [x[0]+value*x[1] for x in zip(self.pos,self.waypoint)]
        else:
            n_turn_clock = value//90 % 4
            if n_turn_clock==1:
                self.waypoint = [self.waypoint[1],-self.waypoint[0]]
            elif n_turn_clock==2:
                self.waypoint = [-self.waypoint[0],-self.waypoint[1]]
            elif n_turn_clock==3:
                self.waypoint = [-self.waypoint[1],self.waypoint[0]]
        return


def manhattan_dist_travelled(directions: List[str],rule: int):
    ship = Ship(rule)
    for d in directions:
        ship.move(d)
    return sum(abs(p) for p in ship.pos)

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        directions = [c.rstrip('\n') for c in f.readlines()]
        
    print('Manhattan distance from start is {0}'.format(manhattan_dist_travelled(directions,1)))
    print('Manhattan distance from start using updated rules is {0}'.format(manhattan_dist_travelled(directions,2)))
    