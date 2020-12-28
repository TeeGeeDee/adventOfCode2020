
TEST = '389125467'
INPUT = '942387615'

def do_moves(str_in,n_moves):
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

                   
if __name__ == '__main__':
    
    print('Part 1 answer = {0}'.format(do_moves(INPUT,100)))
    
