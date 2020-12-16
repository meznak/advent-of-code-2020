import re

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
