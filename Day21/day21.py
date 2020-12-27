
if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        data = [c.rstrip('\n') for c in f.readlines()]
    
    recipies = []
    for row in data:
        ingredients,_,allergens = row.rstrip(')').partition(' (contains ')
        recipies += [(set(ingredients.split(' ')),set(allergens.split(', ')))]
    recipies = tuple(recipies)
    
    allergens_map = {}
    for rec in recipies:
        for a in rec[1]:
            if a not in allergens_map:
                allergens_map[a] = rec[0].copy()
            else:
                allergens_map[a].intersection_update(rec[0])
    taken_ingredients = tuple(list(ing)[0] for ing in allergens_map.values() if len(ing)==1)
    to_rm = taken_ingredients
    while not all(len(ing)==1 for ing in allergens_map.values()):
        [allergens_map[aller].discard(rm) for rm in to_rm for aller in allergens_map if len(allergens_map[aller])>1]
        to_rm = tuple(set(list(ing)[0] for ing in allergens_map.values() if len(ing)==1).difference(taken_ingredients))
    
    print('Part 1 answer = {0}'.format(sum(len(r[0].difference([list(a)[0] for a in allergens_map.values()])) for r in recipies)))
    ingredients_map = {list(allergens_map[aller])[0]:aller for aller in allergens_map}
    print('Part 2 answer = {0}'.format(','.join(sorted(ingredients_map.keys(),key=lambda x: ingredients_map[x]))))
        
