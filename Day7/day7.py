
from typing import List
from itertools import chain

def find_containers(bag_map: dict,bag_colour: str):
    """Return colours of all bags that contain a bag of colour bag_colour.
    

    Parameters
    ----------
    bag_map : dict
        key = colour
        value = dict with key colour of bag, and value the number of that bag contained
    bag_colour : str
        colour of the bag's we wish to find contained

    Returns
    -------
    List[str]
        list of colours of bags containing a bag_colour-d bag (possibly via bag-in-bag etc)

    """
    contains_colour = [b for b in bag_map if bag_colour in bag_map[b]]
    inherited = list(chain(*[find_containers(bag_map,c) for c in contains_colour]))
    return list(set(contains_colour + inherited))

def count_bags(bag_map: dict,bag_colour: str):
    """Return the number of bags contained in the bag of colour bag_colour."""
    this_bag = bag_map[bag_colour]
    return sum(this_bag[c]*(1+count_bags(bag_map,c)) for c in this_bag)

def rules_to_map(rules: List[str]):
    """Return dict of dicts representation of bag contents rules, from list of strings input."""
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

    print('The number colours of bag that contain a shiny gold bag is {0}'.format(len(find_containers(bag_map,'shiny gold'))))
    print('The number of bags contained in the shiny gold bag is {0}'.format(count_bags(bag_map,'shiny gold')))
    