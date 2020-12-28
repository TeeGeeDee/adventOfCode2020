
TEST = '389125467'
INPUT = '942387615'
N = 1000000
N_ITER_PART1 = 100
N_ITER_PART2 = 10000000
N_PICK_OUT = 3

def do_moves_part1(str_in,n_moves):
    x = [int(x) for x in str_in]
    for i in range(n_moves):
        current = x[0]
        pick_up = x.pop(1),x.pop(1),x.pop(1)
        sorted_x = sorted(x)
        destination = sorted_x[sorted_x.index(current)-1]
        ix_new_current = x.index(destination)
        x = x[:ix_new_current+1]+list(pick_up)+x[ix_new_current+1:]
        first = x.pop(0)
        x.append(first)
    ix1 = x.index(1)
    return ''.join(str(y) for y in x[ix1+1:]+x[:ix1])

def mod_end(a,b):
    out = a % b
    if out == 0:
        out = b
    return out

def get_num(ix):
    if len(INPUT)+1 <= ix <= N:
        return ix
    elif 1 <= ix <= len(INPUT):
        return int(INPUT[ix-1])
    else:
        return get_num(mod_end(ix,N))
    
def move(current,d_ll):
    pick_out = []
    x0 = current
    for ii in range(N_PICK_OUT):
        x0 = d_ll[x0][1]
        pick_out.append(x0)
    destination = mod_end(current-1,N)
    while destination in pick_out:
        destination = mod_end(destination-1,N)
    # current to where picked_out pointed to
    d_ll[current][1] = d_ll[pick_out[2]][1]
    d_ll[d_ll[current][1]][0] = current
    # picked out end to where destination pointed to
    d_ll[pick_out[-1]][1] = d_ll[destination][1]
    d_ll[d_ll[pick_out[-1]][1]][0] = pick_out[-1]
    # destination to picked_out start
    d_ll[destination][1] = pick_out[0]
    d_ll[pick_out[0]][0] = destination

    current = d_ll[current][1]
    return current
    

if __name__ == '__main__':
    
    print('Part 1 answer = {0}'.format(do_moves_part1(INPUT,N_ITER_PART1)))
    
    doubly_linked_list = {}
    for ix in range(N):
        ix += 1
        doubly_linked_list[get_num(ix)] = [get_num(ix-1),get_num(ix+1)]

    current = int(INPUT[0])
    for ii in range(N_ITER_PART2):
        current = move(current,doubly_linked_list)
    
    x1 = doubly_linked_list[1][1]
    x2 = doubly_linked_list[x1][1]
    
    print('Part 2 answer = {0}'.format(x1*x2))
   