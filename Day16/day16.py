
from typing import List

def is_valid(value: int,rules: dict):
    return any(bound[0]<=value<=bound[1] for field in rules for bound in rules[field])

def get_valid_mapping(rules: dict,valid_tickets: List[int]):
    valid_pos = {nm:set() for nm in rules}
    for f in rules:
        for pos in range(0,len(valid_tickets[0])):
            if all(is_valid(t[pos], {f:rules[f]}) for t in valid_tickets):
                valid_pos[f].add(pos)
    mapping = {}
    while len(valid_pos)>0:
        field = {k for k in valid_pos if len(valid_pos[k])==1}.pop()
        mapping[field] = valid_pos.pop(field).pop()
        for p in valid_pos:
            valid_pos[p].discard(mapping[field])
    return mapping

def unpack_data(data: List[str]):
    rules = {}
    for d in data:
        if d == '':
            break
        rule_name,bounds = d.split(': ')
        bounds = bounds.split(' or ')
        bounds = [b.split('-') for b in bounds]
        bounds = [[int(b) for b in c] for c in bounds]
        rules[rule_name] = bounds
    
    other_tickets = [[int(x)  for x in ticket.split(',')] for ticket in data[len(rules)+5:]]
    my_ticket = [int(x) for x in data[len(rules)+2].split(',')]
    return rules, my_ticket, other_tickets

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        data = [c.rstrip('\n') for c in f.readlines()]

    rules, my_ticket, other_tickets = unpack_data(data)
    
    print('ticket scanning error rate is {0}'.format(sum(k for t in other_tickets for k in t if not is_valid(k,rules))))

    valid_tickets = [t for t in other_tickets if all(is_valid(f, rules) for f in t)]
    out = get_valid_mapping(rules,valid_tickets)

    product = 1
    for f in out:
        if f.startswith('departure '):
            product *= my_ticket[out[f]]
    
    print('Product is {0}'.format(product))
    