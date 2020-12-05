'''
Advent of Code Day 02
Password validation
'''

import re
from ..shared import read_input, run_solvers

SAMPLE_SOLUTIONS = [2, 1]

def parse_data(dataset: str) -> int:
    '''Interpret passwords and requirements'''
    re_pattern = re.compile(r'(?P<min>\d+)-(?P<max>\d+)\s(?P<char>\w):\s(?P<password>\w+)')

    parsed = []

    for entry in dataset:
        re_match = re_pattern.search(entry).groupdict()
        re_match['min'] = int(re_match['min'])
        re_match['max'] = int(re_match['max'])
        parsed.append(re_match)

    return parsed

def check_password_1(dataset: dict) -> int:
    '''Solve part 1'''

    valid_count = 0

    for entry in dataset:
        chr_count = entry['password'].count(entry['char'])
        if entry['min'] <= chr_count <= entry['max']:
            valid_count += 1

    return valid_count

def check_password_2(dataset: dict) -> int:
    '''Solve part 2'''

    valid_count = 0

    for entry in dataset:
        char = entry['char']
        first = entry['password'][entry['min']-1]
        second = entry['password'][entry['max']-1]

        if (first == char) ^ (second == char):
            valid_count += 1

    return valid_count

if __name__ == '__main__':
    samples, data = read_input(__file__)

    samples_parsed = [parse_data(sample) for sample in samples]
    data_parsed = parse_data(data)

    solvers = [check_password_1, check_password_2]

    run_solvers(samples_parsed, data_parsed, solvers, SAMPLE_SOLUTIONS)
