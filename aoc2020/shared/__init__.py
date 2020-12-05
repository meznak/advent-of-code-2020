import os
from typing import Callable

def read_input(script_file: str) -> ([], []):
    path = os.path.dirname(os.path.realpath(script_file))

    with open(os.path.join(path, 'sample'), 'r') as f:
        sample = [entry.strip() for entry in f.readlines()]

    with open(os.path.join(path, 'input'), 'r') as f:
        data = [entry.strip() for entry in f.readlines()]

    return (sample, data)

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

def run_checks(sample: list, data: list, check_functions: list, \
    sample_solutions: list) -> None:

    for index in [0]:
        result = check_list(sample, data, check_functions[index], \
            sample_solutions[index])
        print(f'result {index}: {result}')