'''
Advent of Code Day 07
Handy Haversacks
'''

import re
from .bag import Bag

SAMPLE_SOLUTIONS = [4, 32]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    re_split = re.compile(r'(?P<color>.*?) bags contain (?P<rules>.*)')

    for item in dataset:
        if item == '':
            continue
        bag_terms = re_split.search(item).groupdict()
        bag = Bag(bag_terms['color'])

        rules = bag_terms['rules'].split(', ')
        re_rule = re.compile(r'(?P<count>\d+) (?P<color>.*?) bag')

        for rule in rules:
            try:
                count, color = re_rule.search(rule).groups()
                bag.add_rule(color, int(count))
            except AttributeError:
                # bag contains no other bags
                pass

        output.append(bag)

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    gold_bag = None
    valid_bags = 0

    for item in dataset:
        item.build_contents(dataset)
        if item.color == 'shiny gold':
            gold_bag = item

    for item in dataset:
        if gold_bag in item.contents:
            valid_bags += 1

    return valid_bags

def solve_2(dataset: list) -> int:
    '''Solve part 2'''
    gold_bag = None
    contained_bag_count = 0

    for item in dataset:
        item.build_contents(dataset)
        if item.color == 'shiny gold':
            gold_bag = item

    contained_bag_count = gold_bag.count_bags()

    return contained_bag_count
