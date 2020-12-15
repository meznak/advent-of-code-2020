'''
Advent of Code Day 15
Rambunctious Recitation
'''

SAMPLE_SOLUTIONS = [436, 175594]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if item != '':
            output = [int(num) for num in item.split(',')]

    return output

def get_nth_number(dataset: list, n: int) -> int:
    '''Returns the number spoken on a given turn'''
    turn = 1
    numbers = {}
    new_number = None

    for new_number in dataset:
        numbers[new_number] = [turn]
        turn += 1

    while turn <= n:
            number = new_number

            if len(numbers[number]) == 1:
                new_number = 0
            else:
                new_number = numbers[number][1] - numbers[number][0]

            if new_number not in numbers:
                numbers[new_number] = [turn]
            else:
                numbers[new_number].append(turn)
                del numbers[new_number][:-2]

            turn += 1

    return new_number

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    return get_nth_number(dataset, 2020)

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    return get_nth_number(dataset, 30000000)