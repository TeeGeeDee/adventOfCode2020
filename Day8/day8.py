
from typing import List

def run_code(code: List[str]):
    acc = 0
    pos = 0
    visited = set()
    reached_end = False
    while pos not in visited:
        visited.update([pos])
        action,n = code[pos][:3],int(code[pos][4:])
        if action == 'acc':
            acc += n
            pos += 1
        elif action == 'jmp':
            pos += n
        elif action == 'nop':
            pos += 1
        if pos==len(code):
            reached_end = True
            break
    return reached_end, acc

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        code = [c.rstrip('\n') for c in f.readlines()]
        
    print('before revisiting a previous state acc was {0}'.format(run_code(code)[1]))
    line = 0
    finished = False
    while not finished:
        mod_code = code.copy()
        if code[line][0:3]=='jmp':
            mod_code[line] = mod_code[line].replace('jmp','nop')
        if code[line][0:3]=='nop':
            mod_code[line] = mod_code[line].replace('nop','jmp')
        if code[line][0:3]=='jmp' or code[line][0:3]=='nop':
            finished,acc = run_code(mod_code)
        line += 1
    print('after fixing the code, at the end acc = {0}'.format(acc))
            
