
from typing import List

def run_code(code: List[str]):
    acc = 0
    i = 0
    visited = set()
    while (i not in visited) and (i<len(code)):
        visited.add(i)
        action,n = code[i][:3],int(code[i][4:])
        if action == 'acc':
            acc += n
            i += 1
        elif action == 'jmp':
            i += n
        elif action == 'nop':
            i += 1

        reached_end = i>=len(code)
    return reached_end, acc

def fix_and_run_code(code: List[str]):
    i = 0
    finished = False
    action_switch = {'jmp':'nop','nop':'jmp'}
    while not finished:
        action = code[i][0:3]
        if action in action_switch:
            mod_code = code.copy()
            mod_code[i] = mod_code[i].replace(action,action_switch[action])
            finished,acc = run_code(mod_code)
        i += 1
    return acc


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        code = [c.rstrip('\n') for c in f.readlines()]
        
    print('before revisiting a previous state acc was {0}'.format(run_code(code)[1]))
    print('after fixing the code, at the end acc = {0}'.format(fix_and_run_code(code)))
            
