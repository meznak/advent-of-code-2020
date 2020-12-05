'''
Advent of Code Day 05
Binary Boarding
'''

import re
from ..shared import read_input, run_solvers

SAMPLE_SOLUTIONS = [820]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''
    output = []

    for entry in dataset:
        entry_b = re.sub('([BR])', '1', entry)
        entry_b = re.sub('([FL])', '0', entry_b)

        row = int('0b' + entry_b[:7], base=2)
        col = int('0b' + entry_b[7:], base=2)

        output.append((row, col))

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    max_id = -999

    for (row, col) in dataset:
        seat_id = row * 8 + col
        if seat_id > max_id:
            max_id = seat_id

    return max_id

def solve_2(dataset: list) -> int:
    '''Solve part 2'''
    for item in dataset:
        # TODO: Build solution
        pass

if __name__ == '__main__':
    samples, data = read_input(__file__)

    samples_parsed = [parse_data(sample) for sample in samples]

    data_parsed = parse_data(data)

    solvers = [solve_1, solve_2]

    run_solvers(samples_parsed, data_parsed, solvers, SAMPLE_SOLUTIONS)
