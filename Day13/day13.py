
from crt import chinese_remainder

def make_crt_input(buses):
    n,a = [],[]
    for i in range(0,len(buses)):
        if buses[i]!='x':
            n.append(int(buses[i]))
            a.append(int(buses[i])-i % int(buses[i]))
    return n,a


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        data = [c.rstrip('\n') for c in f.readlines()]
    
    time = int(data[0])
    buses_raw = data[1]
    
    buses_raw = buses_raw.split(',')
    buses = [int(b) for b in buses_raw if b.isnumeric()]
    
    wait_times = [b- (time % b) for b in buses]
    print('ID multiplied by wait time is {0}'.format(min(wait_times)*buses[wait_times.index(min(wait_times))]))
        
    
    n,a = make_crt_input(buses_raw)
    print('Earliest timestamp is {0}'.format(chinese_remainder(n, a)))
    
    