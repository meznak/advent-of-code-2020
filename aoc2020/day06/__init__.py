'''
Advent of Code Day 06
Custom Customs
'''

SAMPLE_SOLUTIONS = [11, 6]

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

    for group in dataset:
        questions = ''.join(group)
        questions = set(questions)
        total += len(questions)

    return total

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    total = 0

    for group in dataset:
        seen_questions = None

        for person in group:
            questions = set(person)
            if seen_questions is None:
                seen_questions = questions
            else:
                seen_questions &= questions

        total += len(seen_questions)

    return total
