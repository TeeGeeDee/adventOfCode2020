
DOOR_PUBLIC_KEY = 8335663
CARD_PUBLIC_KEY = 8614349


def transform(subject_number,loop_size):
    x = 1
    for ii in range(loop_size):
        x *= subject_number
        x %= 20201227
    return x

def find_loop_size(public_key,subject_number):
    loops = 0
    x = 1
    while x != public_key:
        x *= subject_number
        x %= 20201227
        loops +=1
    return loops

if __name__ == '__main__':
    
    door_loop_num = find_loop_size(DOOR_PUBLIC_KEY, 7)
    print('encryption key = {0}'.format(transform(CARD_PUBLIC_KEY,door_loop_num)))
    