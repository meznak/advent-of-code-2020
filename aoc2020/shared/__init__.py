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

    with open(os.path.join(path, 'sample1'), 'r') as in_file:
        sample_1 = [entry.strip() for entry in in_file.readlines()]

    try:
        with open(os.path.join(path, 'sample2'), 'r') as in_file:
            sample_2 = [entry.strip() for entry in in_file.readlines()]
            if len(sample_2) == 0:
                sample_2 = sample_1
    except FileNotFoundError:
        sample_2 = sample_1
        print('sample2 file not found')

    samples = [sample_1, sample_2]

    with open(os.path.join(path, 'input'), 'r') as in_file:
        data = [entry.strip() for entry in in_file.readlines()]

    return (samples, data)

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

    for index in range(len(solvers)):
        result = solve_list(samples[index], data, solvers[index], \
            sample_solutions[index])
        print(f'result {index}: {result}')
