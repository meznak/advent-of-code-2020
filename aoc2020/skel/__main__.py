# TODO: Add day and title
'''
Advent of Code Day XX
TITLE
'''

from ..shared import read_input, run_checks

# TODO: Add sample solutions
SAMPLE_SOLUTIONS = []

def parse_data(dataset: list) -> list:
    '''Interpret string data'''
    output = []

    for entry in dataset:
        # TODO: Build parser
        pass

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    for item in dataset:
        # TODO: Build solution
        pass

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

    run_checks(samples_parsed, data_parsed, solvers, SAMPLE_SOLUTIONS)
