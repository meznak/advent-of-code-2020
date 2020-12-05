import os
from typing import Callable

def read_input(script_file: str) -> (list, list, list):
    path = os.path.dirname(os.path.realpath(script_file))

    with open(os.path.join(path, 'sample1'), 'r') as f:
        sample1 = [entry.strip() for entry in f.readlines()]

    try:
        with open(os.path.join(path, 'sample2'), 'r') as f:
            sample2 = [entry.strip() for entry in f.readlines()]
    except FileNotFoundError:
        sample2 = None
        print('sample2 file not found')

    samples = [sample1, sample2]

    with open(os.path.join(path, 'input'), 'r') as f:
        data = [entry.strip() for entry in f.readlines()]

    return (samples, data)

def check_list(sample: [str], data: [str], check: Callable[[list], int], \
    sample_solution: int) -> int:
    run_count = 0

    for dataset in [sample, data]:
        result = check(dataset)

        if run_count == 0:
            assert(result == sample_solution), \
                f'''Expected {sample_solution}, got {result}'''
            run_count += 1
        else:
            return result

def run_checks(samples: list, data: list, check_functions: list, \
    sample_solutions: list) -> None:

    for index in range(len(samples)):
        result = check_list(samples[index], data, check_functions[index], \
            sample_solutions[index])
        print(f'result {index}: {result}')