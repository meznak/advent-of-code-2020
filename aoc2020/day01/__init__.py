'''
Advent of Code Day 01
Report Repair
'''

SAMPLE_SOLUTIONS = [514579, 241861950]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = [int(i) for i in dataset if i != '']

    return output

def solve_1(dataset: [int]) -> int:
    '''Solve part 1'''

    for index, a in enumerate(dataset):
        for _, b in enumerate(dataset[index:], index):
            if a + b == 2020:
                return a * b

def solve_2(dataset: [int]) -> int:
    '''Solve part 2'''

    for index, a in enumerate(dataset):
        for index_2, b in enumerate(dataset[index:], index):
            for _, c in enumerate(dataset[index_2:], index_2):
                if a + b + c == 2020:
                    return a * b * c