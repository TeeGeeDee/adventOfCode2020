
def count_active_neighbors(x: int,y: int,z: int,w: int,active_states: set):
    n = 0
    for x_mod in (-1,0,1):
        for y_mod in (-1,0,1):
            for z_mod in (-1,0,1):
                for w_mod in (-1,0,1):
                    if x_mod==0 and y_mod==0 and z_mod==0 and w_mod==0:
                        continue
                    n += (x+x_mod,y+y_mod,z+z_mod,w+w_mod) in active_states
    return n

def update_state(state,is_fourth_dim):
    out_state = state.copy()
    x_bnd,y_bnd,z_bnd,w_bnd = tuple((min(s[d] for s in state)-1,max(s[d] for s in state)+1) for d in range(0,4))
    if not is_fourth_dim:
        w_bnd = (0,0)
    for x in range(x_bnd[0],x_bnd[1]+1):
        for y in range(y_bnd[0],y_bnd[1]+1):
            for z in range(z_bnd[0],z_bnd[1]+1):
                for w in range(w_bnd[0],w_bnd[1]+1):
                    n_active_neigh = count_active_neighbors(x,y,z,w,state)
                    if ((x,y,z,w) in state and (n_active_neigh ==2 or n_active_neigh==3)) or ((x,y,z,w) not in state and n_active_neigh==3):
                        out_state.add((x,y,z,w))
                    else:
                        out_state.discard((x,y,z,w))
    state = out_state
    return state

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        data = [c.rstrip('\n') for c in f.readlines()]

    state = set()
    for ixr,r in enumerate(data):
        for ixs,s in enumerate(r):
            if s=='#':
                state.add((ixs,ixr,0,0))
    start_state = state.copy()
    
    for i in range(0,6):
        state = update_state(state,False)
    print('In 3-d, after 6 cycles there are {0} active states.'.format(len(state)))

    state = start_state
    for i in range(0,6):
        state = update_state(state,True)
    print('In 4-d, after 6 cycles there are {0} active states.'.format(len(state)))
    
    