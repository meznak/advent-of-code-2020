'''
Advent of Code Day 10
Adapter Array
'''

SAMPLE_SOLUTIONS = [220, 19208]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    dataset = [int(item) for item in dataset if item != '']
    dataset.append(0)
    dataset.sort()
    dataset.append(dataset[-1] + 3)

    return dataset

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    ones = 0
    threes = 0

    for i in range(len(dataset) - 1):
        num = dataset[i]
        next_num = dataset[i + 1]
        if next_num == num + 1:
            ones += 1
        elif next_num == num + 3:
            threes += 1

    return ones * threes

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    last_index = len(dataset) - 1
    paths_to_end = [0] * len(dataset)
    paths_to_end[-1] = 1

    for index in range(len(dataset) - 1, -1, -1):
        for next_index in range(index + 1, index + 4):
            if next_index <= last_index and \
                dataset[next_index] <= dataset[index] + 3:
                paths_to_end[index] += paths_to_end[next_index]

    return paths_to_end[0]
