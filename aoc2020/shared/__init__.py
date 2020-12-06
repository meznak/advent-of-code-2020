'''
Shared library for AoC2020 solutions
'''

import os
from typing import Callable

def read_input(script_file: str) -> (list, list, list):
    '''
    Read sample and puzzle input files
    '''

    path = os.path.dirname(os.path.realpath(script_file))

    sample_file = os.path.join(path, 'sample1')
    with open(sample_file, 'r') as in_file:
        sample_1 = [entry.strip() for entry in in_file.readlines()]
        sample_1.append('')

    try:
        sample_file = os.path.join(path, 'sample2')
        if os.stat(sample_file).st_size > 0:
            with open(sample_file, 'r') as in_file:
                sample_2 = [entry.strip() for entry in in_file.readlines()]
                sample_2.append('')
        else:
            sample_2 = sample_1
    except FileNotFoundError:
        sample_2 = sample_1
        print('sample2 file not found')

    samples = [sample_1, sample_2]

    with open(os.path.join(path, 'input'), 'r') as in_file:
        data = [entry.strip() for entry in in_file.readlines()]
        data.append('')

    return (samples, data)

def parse_input(script_file: str, parse_data: Callable[[], list]) -> tuple:
    '''Read and parse data'''
    samples, data = read_input(script_file)

    samples_parsed = [parse_data(sample) for sample in samples]
    data_parsed = parse_data(data)

    return samples_parsed, data_parsed

def solve_list(sample: [str], data: [str], solve: Callable[[list], int], \
    sample_solution: int) -> int:
    '''
    Run solution against sample data, comparing expected results. If
    satisfactory, run solution against puzzle data.
    '''

    run_count = 0

    for dataset in [sample, data]:
        result = solve(dataset)

        if run_count == 0:
            assert(result == sample_solution), \
                f'''Expected {sample_solution}, got {result}'''
            run_count += 1

    return result

def run_solvers(samples: list, data: list, solvers: list, \
    sample_solutions: list) -> None:
    '''
    Run all solutions for the current puzzle
    '''

    for index in range(len(sample_solutions)):
        result = solve_list(samples[index], data, solvers[index], \
            sample_solutions[index])
        print(f'result {index}: {result}')
