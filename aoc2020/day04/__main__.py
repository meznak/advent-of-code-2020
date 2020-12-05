'''
Advent of Code Day 02
Passport verification
'''

import re
from ..shared import read_input, run_solvers

SAMPLE_SOLUTIONS = [2, 4]

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

    def validate_values(self) -> bool:
        '''Validate field contents'''

        is_valid = self.check_dates() and self.check_height() and \
            self.check_hair() and self.check_eyes() and self.check_pid() and \
            self.check_country()

        return is_valid

    def check_dates(self) -> bool:
        '''Verify date ranges

        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        '''
        if  1920 <= int(self.byr) <= 2002 and \
            2010 <= int(self.iyr) <= 2020 and \
            2020 <= int(self.eyr) <= 2030:
            is_valid = True
        else:
            is_valid = False

        return is_valid

    def check_height(self) -> bool:
        '''Verify height

        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        '''

        try:
            hgt = str(self.hgt)
            value = int(hgt[:-2])
            unit = hgt[-2:]

            if unit == 'cm' and 150 <= value <= 193 or \
                unit == 'in' and 59 <= value <= 76:
                is_valid = True
            else:
                is_valid = False
        except (IndexError, TypeError):
            is_valid = False

        return is_valid

    def check_hair(self) -> bool:
        '''Validate hair color
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        '''
        re_pattern = re.compile('^#[0-9a-fA-F]{6}$')
        re_match = re_pattern.search(self.hcl)

        if re_match is not None:
            is_valid = True
        else:
            is_valid = False

        return is_valid

    def check_eyes(self) -> bool:
        '''Validate eye color
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        '''

        if self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            is_valid = True
        else:
            is_valid = False

        return is_valid

    def check_pid(self) -> bool:
        '''Validate passport ID
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        '''

        re_pattern = re.compile(r'^\d{9}$')
        re_match = re_pattern.search(self.pid)

        if re_match is not None:
            is_valid = True
        else:
            is_valid = False

        return is_valid

    def check_country(self) -> bool:
        '''Validate country ID
        cid (Country ID) - ignored, missing or not.
        '''

        # LOLHAX
        return True

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

if __name__ == '__main__':
    samples, data = read_input(__file__)

    samples_parsed = [parse_data(sample) for sample in samples]

    data_parsed = parse_data(data)

    solvers = [solve_1, solve_2]

    run_solvers(samples_parsed, data_parsed, solvers, SAMPLE_SOLUTIONS)
