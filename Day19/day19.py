
def validate(message,rules_map,key):
    any_ok = False
    for opt in rules_map[key]:
        remaining_message = message
        all_ok = True
        for k in range(0,len(opt)):
            rule = opt[k]
            if not rule[0].isnumeric():
                this_ok = remaining_message[0]==rule
                remaining_message = remaining_message[1:]
            else:
                this_ok,remaining_message = validate(remaining_message,rules_map,rule)
            all_ok &= this_ok
            if not all_ok:
                break
        if all_ok:
            any_ok = True
            break
    return any_ok, remaining_message

def check_validity(message,rules_map,key):
    ok,msg = validate(message,rules_map,key)
    return ok and len(msg)==0

# Reddit helped for part 2...
def run_seq(g, seq, s):
    if not seq:
        yield s
    else:
        k, *seq = seq
        for s in run(g, k, s):
            yield from run_seq(g, seq, s)

def run_alt(g, alt, s):
    for seq in alt:
        yield from run_seq(g, seq, s)

def run(g, k, s):
    if isinstance(g[k], list):
        yield from run_alt(g, g[k], s)
    else:
        if s and s[0] == g[k]:
            yield s[1:]

def match(g, s):
    return any(m == '' for m in run(g, '0', s))


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        data = [c.rstrip('\n') for c in f.readlines()]

    i = 0
    while data[i] != '':
        i += 1
    rules = data[:i]
    messages = data[i+1:]
        
    rules_map = {}
    for r in rules:
        k,_,v = r.partition(': ')
        rules_map[k] = [x.split(' ') for x in v.split(' | ')]
        if type(rules_map[k][0][0]) == str and rules_map[k][0][0].startswith('"'):
            rules_map[k] = rules_map[k][0][0][1:-1]
    
    print(sum(check_validity(m,rules_map,'0') for m in messages))

    rules_map['8'] = [['42'],['42','8']]
    rules_map['11'] = [['42','31'],['42','11','31']]
    
    print('P2', sum(match(rules_map, message) for message in messages))
    