
INPUT = '942387615'
N_PICK_OUT = 3

def play_game(str_in,set_size,n_moves):
    doubly_linked_list = {}
    for ix in range(set_size):
        ix += 1
        doubly_linked_list[get_num(ix,set_size)] = [get_num(ix-1,set_size),get_num(ix+1,set_size)]
    
    current = int(str_in[0])
    for ii in range(n_moves):
        current = move(current,doubly_linked_list,set_size)
    return doubly_linked_list

def mod_end(a,b):
    out = a % b
    if out == 0:
        out = b
    return out

def get_num(ix,set_size):
    if len(INPUT)+1 <= ix <= set_size:
        return ix
    elif 1 <= ix <= len(INPUT):
        return int(INPUT[ix-1])
    else:
        return get_num(mod_end(ix,set_size),set_size)
    
def move(current,d_ll,set_size):
    pick_out = []
    x0 = current
    for ii in range(N_PICK_OUT):
        x0 = d_ll[x0][1]
        pick_out.append(x0)
    destination = mod_end(current-1,set_size)
    while destination in pick_out:
        destination = mod_end(destination-1,set_size)
    # current to where picked_out pointed to
    d_ll[current][1] = d_ll[pick_out[2]][1]
    d_ll[d_ll[current][1]][0] = current
    # picked out end to where destination pointed to
    d_ll[pick_out[-1]][1] = d_ll[destination][1]
    d_ll[d_ll[pick_out[-1]][1]][0] = pick_out[-1]
    # destination to picked_out start
    d_ll[destination][1] = pick_out[0]
    d_ll[pick_out[0]][0] = destination

    return d_ll[current][1]
    

if __name__ == '__main__':
    
    d_ll_1 = play_game(INPUT,9,100)
    out = []
    current = d_ll_1[1][1]
    while current != 1:
        out.append(current)
        current = d_ll_1[current][1]
    print('Part 1 answer = {0}'.format(''.join(str(y) for y in out)))
    
    d_ll_2 = play_game(INPUT,1000000,10000000)
    
    x1 = d_ll_2[1][1]
    x2 = d_ll_2[x1][1]
    print('Part 2 answer = {0}'.format(x1*x2))
   