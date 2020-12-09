
from typing import List

def run_code(code: List[str]):
    """Return accumulator after code either enters infinite loop or reaches end.
    
    Parameters
    ----------
    code : List[str]
        each element starts with one of: acc,jmp,nop and then ' ' and then a signed number
        These actions are:
            acc - add number to accumulator (starts at 0), then go to next line
            jmp - move position specified by the number (e.g. +1 = 'go to next line')
            nop - go to next line
    
    Returns
    -------
    reached_end: bool
        true if code ran to end without hiting infinite loop
    accumulator: int
        count kept when stepping through code (modified by 'acc' steps)
    
    """
    accumulator = 0
    i = 0
    visited = set()
    while (i not in visited) and (i<len(code)):
        visited.add(i)
        action,_,n = code[i].partition(' ')
        n = int(n)
        if action == 'acc':
            accumulator += n
            i += 1
        elif action == 'jmp':
            i += n
        elif action == 'nop':
            i += 1
        reached_end = i>=len(code)
    return reached_end, accumulator

def fix_and_run_code(code: List[str]):
    """Fix jmp/nop line (to nop/jmp) that results in infinite loop, then run and output accumulator"""
    i = 0
    finished = False
    swap = {'jmp':'nop','nop':'jmp'}
    while not finished:
        action = code[i].partition(' ')[0]
        if action in swap:
            mod_code = code.copy()
            mod_code[i] = mod_code[i].replace(action,swap[action])
            finished,accumulator = run_code(mod_code)
        i += 1
    return accumulator


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        code = [c.rstrip('\n') for c in f.readlines()]
        
    print('Before revisiting a previous state acc was {0}'.format(run_code(code)[1]))
    print('After fixing the code, at the end acc is {0}'.format(fix_and_run_code(code)))
            
