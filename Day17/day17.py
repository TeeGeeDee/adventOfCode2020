
def count_active_neighbors(x: int,y: int,z: int,active_states: set):
    n = 0
    for x_mod in (-1,0,1):
        for y_mod in (-1,0,1):
            for z_mod in (-1,0,1):
                if x_mod==0 and y_mod==0 and z_mod==0:
                    continue
                n += (x+x_mod,y+y_mod,z+z_mod) in active_states
    return n

def update_state(state):
    out_state = state.copy()
    x_bnd,y_bnd,z_bnd = tuple((min(s[d] for s in state)-1,max(s[d] for s in state)+1) for d in range(0,3))
    for x in range(x_bnd[0],x_bnd[1]+1):
        for y in range(y_bnd[0],y_bnd[1]+1):
            for z in range(z_bnd[0],z_bnd[1]+1):
                n_active_neigh = count_active_neighbors(x,y,z,state)
                if ((x,y,z) in state and (n_active_neigh ==2 or n_active_neigh==3)) or ((x,y,z) not in state and n_active_neigh==3):
                    out_state.add((x,y,z))
                else:
                    out_state.discard((x,y,z))
    state = out_state
    return state

if __name__ == '__main__':
    
    with open("test.txt", "r") as f:
        data = [c.rstrip('\n') for c in f.readlines()]

    state = set()
    for ixr,r in enumerate(data):
        for ixs,s in enumerate(r):
            if s=='#':
                state.add((ixs,ixr,0))
    
    print('number of active states to start = {0}'.format(len(state)))
    for i in range(0,6):
        state = update_state(state)
        print('number of active states after {0} updates is {1}'.format(i+1,len(state)))
    print('After 6 cycles there are {0} active states.'.format(len(state)))
