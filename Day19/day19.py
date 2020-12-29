
def validate(message,rules_map,key):
    any_ok = False
    for opt in rules_map[key]:
        remaining_message = message
        all_ok = True
        for k in range(0,len(opt)):
            rule = opt[k]
            if rule.startswith('"'):
                this_ok = remaining_message[0]==rule[1]
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
    
    print(sum(check_validity(m,rules_map,'0') for m in messages))

    rules_map['8'] = [['42'],['42','8']]
    rules_map['11'] = [['42','31'],['42','11','31']]
    