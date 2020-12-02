from ..shared import read_input
import re

sample_solution_1 = 2
sample_solution_2 = -1

def parse_data(data: str) -> int:
    p = re.compile('(?P<min>\d+)-(?P<max>\d+)\s(?P<chr>\w):\s(?P<password>\w+)')

    valid_count = 0

    for entry in data:
        m = p.search(entry).groupdict()
        chr_count = m['password'].count(m['chr'])
        if int(m['min']) <= chr_count <= int(m['max']):
            valid_count += 1

    return valid_count

def check_list_1(sample: dict, data: dict, sample_solution: int) -> int:
    valid_count = parse_data(sample)
    assert(valid_count == sample_solution), \
        f'''Expected {sample_solution}, got {valid_count}'''
    valid_count = parse_data(data)

    return valid_count

if __name__ == '__main__':
    sample, data = read_input(__file__)

    valid_count = check_list_1(sample, data, sample_solution_1)
    print(f'part 1: {valid_count}')