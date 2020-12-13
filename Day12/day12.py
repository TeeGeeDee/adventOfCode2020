
DIRECTIONS = ('N','E','S','W')

class Ship:
    def __init__(self):
        self.facing = 'E'
        self.pos = [0,0]
        self.waypoint = [10,1]
    
    def move(self,instruction: str):
        action,value = instruction[0],int(instruction[1:])
        if action == 'F':
            action = self.facing

        if action in ('L','S','W'):
            value = -1*value

        if action in DIRECTIONS:
            if action in ('N','S'):
                self.pos[0] = self.pos[0]+value
            else:
                self.pos[1] = self.pos[1]+value
        else:
            ix_dir = DIRECTIONS.index(self.facing)
            self.facing = DIRECTIONS[(ix_dir + int(value/90)) % len(DIRECTIONS)]
        return

    def move2(self,instruction: str):
        action,value = instruction[0],int(instruction[1:])
        if action in ('L','S','W'):
            value = -1*value
    
        if action in DIRECTIONS:
            if action in ('N','S'):
                self.waypoint[1] = self.waypoint[1]+value
            else:
                self.waypoint[0] = self.waypoint[0]+value
        elif action =='F':
            self.pos[0] += int(value*self.waypoint[0])
            self.pos[1] += int(value*self.waypoint[1])
        else:
            n_rot_right = int(value/90) % 4
            if n_rot_right==1:
                self.waypoint = [self.waypoint[1],-self.waypoint[0]]
            elif n_rot_right==2:
                self.waypoint = [-self.waypoint[0],-self.waypoint[1]]
            elif n_rot_right==3:
                self.waypoint = [-self.waypoint[1],self.waypoint[0]]
        return

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        directions = [c.rstrip('\n') for c in f.readlines()]
    
    ship = Ship()
    for d in directions:
        ship.move(d)
        
    ship2 = Ship()
    for d in directions:
        ship2.move2(d)
        
    print('Manhattan distance from start is {0}'.format(sum(abs(p) for p in ship.pos)))
    print('Manhattan distance from start using updated rules is {0}'.format(sum(abs(p) for p in ship2.pos))) 
    