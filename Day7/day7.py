
from typing import List
from itertools import chain

def find_containers(bag_map: dict,colour: str):
    contains_colour = [b for b in bag_map if colour in bag_map[b]]
    inherited = list(chain(*[find_containers(bag_map,c) for c in contains_colour]))
    return list(set(contains_colour + inherited))

def count_bags(bag_map: dict,colour: str):
    this_bag = bag_map[colour]
    return sum(this_bag[c]*(1+count_bags(bag_map,c)) for c in this_bag)

def rules_to_map(rules: List[str]):
    rules = [r.replace('bags','bag').replace(' bag.','') for r in rules]
    bag_map = dict()
    for r in rules:
        bag,contents = r.split(' bag contain ')
        contents = contents.split(' bag, ')
        contents = [b.partition(' ') for b in contents if b != 'no other']
        bag_map[bag] = {b[2]:int(b[0]) for b in contents}
    return bag_map


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        rules = [r.rstrip('\n') for r in f.readlines()]

    bag_map = rules_to_map(rules)

    print('ans 1 = {0}'.format(len(find_containers(bag_map,'shiny gold'))))
    print('ans 2 = {0}'.format(count_bags(bag_map,'shiny gold')))
    