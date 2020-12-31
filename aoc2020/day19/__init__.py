'''
Advent of Code Day 19
Monster Messages
'''

import re
from copy import deepcopy

SAMPLE_SOLUTIONS = [2]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    rules = {}
    data = []
    section = 0

    re_rule = re.compile(r'(?P<number>\d+): (?P<rule>.*)')

    for item in dataset:
        if item == '':
            section += 1
            continue

        if section == 0:
            number, rule = re_rule.match(item).groups()
            number = int(number)
            rules[number] = []

            for sub_rule in rule.strip('"').split('|'):
                sub_rule_list = []

                for char in sub_rule.strip(' ').split(' '):
                    # Make numbers numbers. Leave alpha characters alone.
                    try:
                        char = int(char)
                    except ValueError:
                        pass

                    sub_rule_list.append(char)

                rules[number].append(sub_rule_list)
        else:
            data.append(item)

    return [rules, data]

def simplify_rules(rules: dict) -> list:
    changed = True

    while changed:
        changed = False
        for to_replace in deepcopy(rules):
            for rule in rules:
                if rule == to_replace:
                    continue

                to_delete = []

                for i, sub_rule in enumerate(rules[rule]):
                    sub_rule = deepcopy(sub_rule)
                    for j, token in enumerate(sub_rule):
                        if token == to_replace:
                            try:
                                new_sub = [rules[rule][i][:j] + sub + rules[rule][i][j + 1:] for sub in rules[token]]
                                changed = True
                            except IndexError:
                                pass


                            [rules[rule].append(new_sub_rule) for new_sub_rule in new_sub]
                    to_delete.append((j, i))

                for j, i in sorted(to_delete, reverse = True):
                    del rules[rule][i][j]


            if changed:
                del rules[to_replace]
                break

    return rules

def check_string_matches(string: str, rules: dict) -> bool:


    return matches

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    all_strings = simplify_rules(dataset[0])
    print(all_strings)

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
