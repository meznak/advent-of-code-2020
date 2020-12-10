'''
Advent of Code Day 09
Encoding Error
'''

SAMPLE_SOLUTIONS = [127, 62]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    dataset = [int(item) for item in dataset if item != '']

    return dataset

def find_pair(dataset: list, index: int, window: int) -> bool:
    '''Find a pair of numbers that adds to the one at index'''

    for i in range(index - window, index - 1):
        for j in range(i, index):
            if dataset[i] + dataset[j] == dataset[index]:
                return True

    return False

def find_sequence(dataset: list, target: int) -> list:
    '''Find a contiguous sequence that adds to target'''

    for i in range(len(dataset)):
        sequence_sum = dataset[i]
        for j in range(i + 1, len(dataset)):
            sequence_sum += dataset[j]
            if sequence_sum > target:
                break
            if sequence_sum == target:
                return dataset[i:j + 1]
    return []

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

    target = solve_1(dataset)

    found_sequence = find_sequence(dataset, target)
    if len(found_sequence) > 0:
        found_sequence.sort()
        return found_sequence[0] + found_sequence[-1]

    return -1