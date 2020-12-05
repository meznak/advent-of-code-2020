'''
Advent of Code Day 02
Passport verification
'''

import re
from ..shared import read_input, run_checks

SAMPLE_SOLUTION_1 = 2

class Passport:
    '''Contains fields on a passport'''
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

def parse_data(dataset: list) -> list:
    '''Interpret string data as Passport'''
    passports = []

    record = None

    dataset.append('')

    for line in dataset:
        if line != '':
            if record is None:
                record = line
            else:
                record = ' '.join([record, line])
        else:
            passport = Passport()

            fields = record.split(' ')
            record = None

            re_pattern = re.compile('(?P<key>[^:]+):(?P<value>.*)')
            for field in fields:
                if field == '':
                    continue
                re_match = re_pattern.search(field).groupdict()
                setattr(passport, re_match['key'], re_match['value'])

            passports.append(passport)
            del passport

    return passports

def check_1(dataset: list) -> int:
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

if __name__ == '__main__':
    sample, data = read_input(__file__)

    sample_parsed = parse_data(sample)
    data_parsed = parse_data(data)

    run_checks(sample_parsed, data_parsed, [check_1],\
        [SAMPLE_SOLUTION_1])
