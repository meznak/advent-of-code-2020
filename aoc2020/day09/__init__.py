'''
Advent of Code Day 09
Encoding Error
'''

SAMPLE_SOLUTIONS = [127]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    dataset = [int(item) for item in dataset if item != '']

    return dataset

def find_pair(dataset: list, index: int, window: int) -> bool:
    for i in range(index - window, index - 1):
        for j in range(i, index):
            if dataset[i] + dataset[j] == dataset[index]:
                return True
    return False

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    dataset_len = len(dataset)
    if dataset_len < 25:
        window = 5
    else:
        window = 25

    for index in range(window, dataset_len):
        found_pair = find_pair(dataset, index, window)
        if not found_pair:
            return dataset[index]

    return -1

def solve_2(dataset: list) -> int:
    '''Solve part 2'''
    for item in dataset:
        # TODO: Build solution
        pass
