'''
Advent of Code Day 22
Crab Combat
'''

SAMPLE_SOLUTIONS = [306]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []
    player = 0
    player_1 = []
    player_2 = []

    for item in dataset:
        if item == '':
            continue

        if item[0] == 'P':
            player += 1
            continue

        if player == 1:
            player_1.append(int(item))
        else:
            player_2.append(int(item))

    return [player_1, player_2]

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    player_1 = list(reversed(dataset[0]))
    player_2 = list(reversed(dataset[1]))

    while len(player_1) and len(player_2):
        p1_top = player_1.pop()
        p2_top = player_2.pop()

        if p1_top > p2_top:
            player_1.insert(0, p1_top)
            player_1.insert(0, p2_top)
        else:
            player_2.insert(0, p2_top)
            player_2.insert(0, p1_top)

    multiplier = 1
    score = 0

    for player in [player_1, player_2]:
        if len(player):
            for card in player:
                score += card * multiplier
                multiplier += 1

    return score

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
