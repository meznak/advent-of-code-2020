'''
Advent of Code Day 21
Allergen Assessment
'''

import re

SAMPLE_SOLUTIONS = [5]

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

def find_possibles(allergens: dict) -> set:
    possibles = set()

    for allergen in allergens:
        temp = None
        for ingredients in allergens[allergen]:
            if temp is None:
                temp = ingredients

            temp = temp.intersection(ingredients)

        possibles = possibles.union(temp)

    return possibles

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    allergens = dataset[0]
    all_ingredients = dataset[1]

    possibles = find_possibles(allergens)
    safe = set(all_ingredients) - possibles

    count = 0
    for ingredient in safe:
        count += all_ingredients.count(ingredient)

    return count

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
