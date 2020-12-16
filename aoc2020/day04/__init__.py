'''
Advent of Code Day 02
Passport Processing
'''

import re
from .passport import Passport

SAMPLE_SOLUTIONS = [2, 4]


def parse_data(dataset: list) -> list:
    '''Interpret string data as Passport'''
    passports = []

    record = None

    if dataset[-1] != '':
        dataset.append('')

    for item in dataset:
        if item != '':
            if record is None:
                record = item
            else:
                record = ' '.join([record, item])
        else:
            passport = Passport()

            fields = record.split(' ')
            record = None

            re_pattern = re.compile(r'(?P<key>[^:]+):(?P<value>.*)')
            for field in fields:
                if field == '':
                    continue
                re_match = re_pattern.search(field).groupdict()
                setattr(passport, re_match['key'], re_match['value'])

            passports.append(passport)
            del passport

    return passports

def solve_1(dataset: list) -> int:
    '''Solve part 1'''
    valid_count = 0

    for item in dataset:
        is_valid = True

        for pass_property in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if getattr(item, pass_property) is None:
                is_valid = False
                break

        if is_valid:
            valid_count += 1

    return valid_count

def solve_2(dataset: list) -> int:
    '''Solve part 2'''
    valid_count = 0

    for item in dataset:
        is_valid = True

        for pass_property in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if getattr(item, pass_property) is None:
                is_valid = False
                break

        if is_valid:
            if item.validate_values():
                valid_count += 1

    return valid_count
