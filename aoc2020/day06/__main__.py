'''
Advent of Code Day 06
Custom Customs
'''

from ..shared import read_input, run_solvers

SAMPLE_SOLUTIONS = [11]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''
    output = []
    group = []

    for entry in dataset:
        if entry != '':
            group.append(entry)
        else:
            output.append(group)
            group = []

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    total = 0

    for item in dataset:
        questions = ''.join(item)
        questions = set(list(questions))
        total += len(questions)

    return total

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
