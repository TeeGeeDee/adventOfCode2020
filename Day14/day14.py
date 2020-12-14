
from typing import List

def int2bin(i: int):
    return str(bin(i))[2:].rjust(36,'0')

def apply_mask(n: str,mask: str):
    b = int2bin(int(n))
    masked_b = ''
    for i in range(0,len(b)):
        if mask[i]=='X':
            masked_b += b[i]
        else:
            masked_b +=mask[i]
    return masked_b

def apply_mask2(n: str,mask: str):
    b = int2bin(int(n))
    masked_b = ''
    for i in range(0,len(b)):
        if mask[i] == 'X':
            masked_b += 'X'
        elif mask[i] == '0':
            masked_b += b[i]
        elif mask[i] == '1':
            masked_b += '1'
    return masked_b

def run_code2(code: List[str]):
    mem = {}
    for r in code:
        if r[0:4]=='mask':
            _,mask = r.split(' = ')
        else:
            mem_pos,val = r[4:].split('] = ')
            positions = expand([apply_mask2(mem_pos,mask)])
            for p in positions:
                mem[int(p,2)] = int(val)
    return sum(v for v in mem.values())

def expand(s):
    if 'X' not in s[0]:
        return s
    else:
        out = []
        for ss in s:
            p1,_,p2 = ss.partition('X')
            out += [p1+'0'+p2,p1+'1'+p2]
        return expand(out)

def run_code(code: List[str]):
    mem = {}
    for r in code:
        if r[0:4]=='mask':
            _,mask = r.split(' = ')
        else:
            mem_pos,val = r[4:].split('] = ')
            mem[mem_pos] = apply_mask(val,mask)
    return sum(int(v,2) for v in mem.values())


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        code = [c.rstrip('\n') for c in f.readlines()]
        
    print('Sum of values in memory is {0}'.format(run_code(code)))
    print('Sum of values in memory for v2 is {0}'.format(run_code2(code)))
        