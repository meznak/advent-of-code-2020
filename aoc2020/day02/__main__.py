from ..shared import read_input
from typing import Callable
import re

sample_solution_1 = 2
sample_solution_2 = 1

def parse_data(data: str) -> int:
    p = re.compile('(?P<min>\d+)-(?P<max>\d+)\s(?P<chr>\w):\s(?P<password>\w+)')

    parsed = []

    for entry in data:
        m = p.search(entry).groupdict()
        m['min'] = int(m['min'])
        m['max'] = int(m['max'])
        parsed.append(m)

    return parsed

def check_password_1(entry: dict) -> int:
    chr_count = entry['password'].count(entry['chr'])
    if entry['min'] <= chr_count <= entry['max']:
        is_valid = 1
    else:
        is_valid = 0

    return is_valid

def check_password_2(entry: dict) -> int:
    if entry['password'][entry['min']-1] == entry['chr'] or \
        entry['password'][entry['max']-1] == entry['chr']:
        is_valid = 1
    else:
        is_valid = 0

    return is_valid

def check_list(sample: dict, data: dict, \
    check: Callable[[int, int, str, str], int], sample_solution: int) -> int:

    run_count = 0
    for dataset in [sample, data]:
        valid_count = 0
        parsed = parse_data(dataset)

        for entry in parsed:
            valid_count += check(entry)

        if run_count == 0:
            assert(valid_count == sample_solution), \
                f'''Expected {sample_solution}, got {valid_count}'''
            run_count += 1
        else:
            return valid_count

if __name__ == '__main__':
    sample, data = read_input(__file__)

    valid_count = check_list(sample, data, check_password_1, sample_solution_1)
    print(f'part 1: {valid_count}')

    valid_count = check_list(sample, data, check_password_2, sample_solution_2)
    print(f'part 2: {valid_count}')