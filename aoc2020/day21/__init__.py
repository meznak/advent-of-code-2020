'''
Advent of Code Day 21
Allergen Assessment
'''

import re

SAMPLE_SOLUTIONS = [5, 'mxmxvkd,sqjhc,fvjkl']

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    all_allergens = {}
    all_ingredients_list = []

    re_pattern = re.compile(r'(?P<ingredients>[^\(]+)\(contains (?P<allergens>[^\)]+)')

    for item in dataset:
        if item == '':
            continue

        ingredients, allergens = re_pattern.search(item).groups()
        ingredients = ingredients.strip(' ').split(' ')
        allergens = allergens.split(', ')

        all_ingredients_list += ingredients

        for allergen in allergens:
            if allergen not in all_allergens:
                all_allergens[allergen] = []

            all_allergens[allergen].append(set(ingredients))

    return [all_allergens, all_ingredients_list]

def find_possibles(allergens: dict) -> dict:
    '''Find possible ingredients for each allergen'''
    possibles = dict()

    for allergen in allergens:
        temp = None
        for ingredients in allergens[allergen]:
            if temp is None:
                temp = ingredients

            temp = temp.intersection(ingredients)

        possibles[allergen] = temp

    return possibles

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    allergens = dataset[0]
    all_ingredients = dataset[1]
    danger = set()

    possibles_by_allergen = find_possibles(allergens)

    for allergen in possibles_by_allergen:
        danger = danger.union(possibles_by_allergen[allergen])

    safe = set(all_ingredients) - danger

    count = 0
    for ingredient in safe:
        count += all_ingredients.count(ingredient)

    return count

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    allergens = dataset[0]
    danger = set()

    possibles_by_allergen = find_possibles(allergens)

    changed = True

    while changed:
        changed = False
        for allergen in possibles_by_allergen:
            if len(possibles_by_allergen[allergen]) == 1:
                ingredient = possibles_by_allergen[allergen]
                for next_allergen in possibles_by_allergen:
                    if next_allergen == allergen:
                        continue

                    new_next = possibles_by_allergen[next_allergen] - ingredient
                    if new_next != possibles_by_allergen[next_allergen]:
                        possibles_by_allergen[next_allergen] = new_next
                        changed = True

    danger = [possibles_by_allergen[p] for p in sorted(possibles_by_allergen)]
    danger_list = ','.join([''.join(list(d)) for d in danger])
    return danger_list
