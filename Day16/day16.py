
from typing import List

def is_valid(fld: int,rules: List[List[List[int]]]):
    all_rules = [item for sublist in rules for item in sublist]
    is_fld_valid = False
    for r in all_rules:
        if r[0]<=fld<=r[1]:
            is_fld_valid = True
            break
    return is_fld_valid

def get_valid_combo(valid_pos: dict):
    out = {}
    valid_pos = {k:set(valid_pos[k]) for k in valid_pos}
    while len(valid_pos)>0:
        for k in valid_pos:
            if len(valid_pos[k])==1:
                out[k] = valid_pos.pop(k).pop()
                for p in valid_pos:
                    valid_pos[p].discard(out[k])
                break
    return out


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        data = [c.rstrip('\n') for c in f.readlines()]

    rules = []
    rule_names = []
    for d in data:
        if d == '':
            break
        rule_name,bounds = d.split(': ')
        bounds = bounds.split(' or ')
        bounds = [b.split('-') for b in bounds]
        bounds = [[int(b) for b in c] for c in bounds]
        rules.append(bounds)
        rule_names.append(rule_name)
    
    other_tickets = []
    for ii in range(len(rules)+5,len(data)):
        other_tickets.append([int(d) for d in data[ii].split(',')])
    
    my_ticket = [int(d) for d in data[len(rules)+2].split(',')]
    
    print('ticket scanning error rate is {0}'.format(sum(k for t in other_tickets for k in t if not is_valid(k,rules))))

    valid_tickets = [t for t in other_tickets if all(is_valid(f, rules) for f in t)]
    
    valid_pos = {nm:[] for nm in rule_names}
    for k in range(0,len(rules)):
        r = rules[k]
        for i in range(0,len(valid_tickets[0])):
            is_val = True
            for j in range(0,len(valid_tickets)):
                is_val &= is_valid(valid_tickets[j][i], [rules[k]])
                if not is_val:
                    break
            if is_val:
                valid_pos[rule_names[k]].append(i)
    
    out = get_valid_combo(valid_pos)
    product = 1
    for f in out:
        if f.startswith('departure '):
            product *= my_ticket[out[f]]
    
    print('Product is {0}'.format(product))
    