
from typing import Callable

def eval_lr(formula: str):
    ix = formula.find(' ')
    if ix ==-1 or ix == len(formula)-1:
        return formula
    lhs,_,rhs = formula.partition(' ')
    operation,_,rhs = rhs.partition(' ')
    rhs,_,remainder = rhs.partition(' ')
    if len(remainder)>0:
        remainder = ' ' + remainder
    return eval_lr(str(eval(lhs+operation+rhs))+remainder)

def eval_switched_precidence(formula: str):
    while formula.find('+') != -1:
        ix_start = formula.find('+')-2
        ix_end = formula.find('+')+2
        while ix_start>0 and formula[ix_start] != ' ':
            ix_start -= 1
        while ix_end<len(formula) and formula[ix_end] != ' ':
            ix_end += 1
        start_formula = formula[:ix_start]
        if len(start_formula)>0:
            start_formula = start_formula + ' '
        end_formula = formula[ix_end+1:]
        if len(end_formula)>0:
            end_formula = ' ' + end_formula
        formula = start_formula +  str(eval(formula[ix_start:ix_end])) + end_formula
    return str(eval(formula))


def eval_formula(formula: str,eval_fn: Callable):
    while formula.find(')') != -1:
        ix_end = formula.index(')')
        ix_start = ix_end
        while formula[ix_start] != '(':
            ix_start -= 1
        formula = formula[:ix_start] + eval_fn(formula[ix_start+1:ix_end]) + formula[ix_end+1:]
    return int(eval_fn(formula))
    

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        formulas = [c.rstrip('\n') for c in f.readlines()]
    
    print('Part 1 sum of answers is {0}'.format(sum(eval_formula(f,eval_lr) for f in formulas)))
    print('Part 2 sum of answers is {0}'.format(sum(eval_formula(f,eval_switched_precidence) for f in formulas)))
    