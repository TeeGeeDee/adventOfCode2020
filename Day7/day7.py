
from itertools import chain

def find_bags_im_in(bag_map: dict,colour: str):
    contains_colour = [b for b in bag_map if colour in bag_map[b]]
    inherited = list(chain(*[find_bags_im_in(bag_map,c) for c in contains_colour]))
    return list(set(contains_colour + inherited))

def count_bags(bag_map: dict,colour: str):
    this_bag = bag_map[colour]
    return sum([this_bag[c]*(1+count_bags(bag_map,c)) for c in this_bag])
    

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        rules = [r.rstrip('\n') for r in f.readlines()]
    rules = [r.replace(' bags.','').replace(' bag.','') for r in rules]
    
    bag_map = dict()
    for r in rules:
        container,contains = r.split(' bags contain ')
        contains = [r.split(' bag, ') for r in contains.split(' bags, ')]
        contains = list(chain(*contains))
        if contains==['no other']:
            contains = []
        contains = {b[b.find(' ')+1:]:int(b[:b.find(' ')]) for b in contains}
        bag_map[container] = contains

    tgd = find_bags_im_in(bag_map,'shiny gold')
    print('ans 1 = {0}'.format(len(find_bags_im_in(bag_map,'shiny gold'))))
    print('ans 2 = {0}'.format(count_bags(bag_map,'shiny gold')))
    