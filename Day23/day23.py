
INPUT = '942387615'
N_PICK_OUT = 3

def play_game(str_in,set_size,n_moves):
    linked_list = {}
    for ix in range(set_size):
        ix += 1
        linked_list[get_num(ix,set_size)] = get_num(ix+1,set_size)
    
    current = int(str_in[0])
    for ii in range(n_moves):
        current = move(current,linked_list,set_size)
    return linked_list

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
    
def move(current,ll,set_size):
    pick_out = []
    x0 = current
    for ii in range(N_PICK_OUT):
        x0 = ll[x0]
        pick_out.append(x0)
    destination = mod_end(current-1,set_size)
    while destination in pick_out:
        destination = mod_end(destination-1,set_size)
    ll[current]      = ll[pick_out[2]]
    ll[pick_out[-1]] = ll[destination]
    ll[destination]  = pick_out[0]

    return ll[current]
    

if __name__ == '__main__':
    
    ll_1 = play_game(INPUT,9,100)
    out = []
    current = ll_1[1]
    while current != 1:
        out.append(current)
        current = ll_1[current]
    print('Part 1 answer = {0}'.format(''.join(str(y) for y in out)))
    
    ll_2 = play_game(INPUT,1000000,10000000)
    
    x1 = ll_2[1]
    x2 = ll_2[x1]
    print('Part 2 answer = {0}'.format(x1*x2))
   