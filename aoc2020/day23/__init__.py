'''
Advent of Code Day 23
Crab Cups
'''

SAMPLE_SOLUTIONS = ['67384529']

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    for item in dataset:
        if item != '':
            output = [int(number) for number in item]

    return output

def play_game(cups: list, rounds: int) -> list:
    '''Play the "game"'''
    # Pick a starting cup
    current_index = 0
    next_label = cups[current_index]

    for _ in range(rounds):
        current_label = next_label
        current_index = cups.index(current_label)

        # Rotate the list to make mod math easier
        if current_index > len(cups) - 4:
            cups = [cups[(i + 3) % len(cups)] for i, x in enumerate(cups)]
            current_index -= 3

        # Pick up three cups clockwise
        picked_up = []

        for __ in range(3):
            picked_up.append(cups.pop((current_index + 1) % len(cups)))

        # Select a destination cup either 1 less than current's label or max of
        # remaining labels
        target_label = current_label - 1

        while target_label not in cups:
            target_label -= 1
            if target_label < min(cups):
                target_label = max(cups)
                break

        target_index = cups.index(target_label)

        # Place cups to the right of the target
        for cup in reversed(picked_up):
            cups.insert(target_index + 1, cup)

        # Make the next clockwise cup the new current cup
        next_label = cups[(cups.index(current_label) + 1) % len(cups)]

    return cups

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    cups = dataset

    cups = play_game(cups, 100)

    # Rotate list so cup 1 is first
    index_of_1 = cups.index(1)
    cups = [cups[(i + index_of_1) % len(cups)] for i, x in enumerate(cups)]

    # Report cups to the right of cup 1
    return ''.join([str(cup) for cup in cups[1:]])

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
