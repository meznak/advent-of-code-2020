'''
Advent of Code Day 02
Password Philosophy
'''

import re

SAMPLE_SOLUTIONS = [2, 1]

def parse_data(dataset: str) -> int:
    '''Interpret passwords and requirements'''
    re_pattern = re.compile(r'(?P<min>\d+)-(?P<max>\d+)\s(?P<char>\w):\s(?P<password>\w+)')

    parsed = []

    for entry in dataset:
        if entry == '':
            continue

        re_match = re_pattern.search(entry).groupdict()
        re_match['min'] = int(re_match['min'])
        re_match['max'] = int(re_match['max'])
        parsed.append(re_match)

    return parsed

def solve_1(dataset: dict) -> int:
    '''Solve part 1'''

    valid_count = 0

    for entry in dataset:
        chr_count = entry['password'].count(entry['char'])
        if entry['min'] <= chr_count <= entry['max']:
            valid_count += 1

    return valid_count

def solve_2(dataset: dict) -> int:
    '''Solve part 2'''

    valid_count = 0

    for entry in dataset:
        char = entry['char']
        first = entry['password'][entry['min'] - 1]
        second = entry['password'][entry['max'] - 1]

        if (first == char) ^ (second == char):
            valid_count += 1

    return valid_count
