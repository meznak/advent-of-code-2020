'''
Advent of Code Day 07
Handy Haversacks
'''

from copy import copy
import re

SAMPLE_SOLUTIONS = [4, 32]

class Bag:
    '''Describes a bag and its contents'''

    def __init__(self, color: str) -> None:
        self.found_contents = False
        self.color = color
        self.contents = set()
        self.rules = dict()

    def add_rule(self, color: str, count) -> None:
        '''Adds a rule about contained bags'''

        self.rules[color] = count

    def build_contents(self, bags: list) -> None:
        '''Constructs a set of all contained bags'''

        changed = True

        while changed:
            own_contents = copy(self.contents)

            changed = False
            if len(self.rules) != 0 and len(self.contents) == 0:
                # Start with a bag's own contents
                for rule in self.rules:
                    for bag in bags:
                        if bag.color == rule:
                            own_contents |= {bag}
                            break

                self.contents |= own_contents
                changed = True

            for bag in self.contents:
                if not bag.found_contents:
                    bag.build_contents(bags)
                own_contents |= bag.contents

                if self.contents != own_contents:
                    own_contents |= self.contents
                    changed = True

            self.contents = own_contents
            self.found_contents = True

    def count_bags(self) -> int:
        '''Count bags contained in this bag'''

        contained_bag_count = 0

        for bag in self.contents:
            if bag.color in self.rules:
                sub_count = bag.count_bags()
                multiplier = self.rules[bag.color]
                contained_bag_count += (sub_count + 1) * multiplier

        return contained_bag_count

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
