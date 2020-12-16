'''
Advent of Code Day 05
Binary Boarding
'''

import re

SAMPLE_SOLUTIONS = [820, 568]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''
    output = []

    for entry in dataset:
        if entry == '':
            continue

        entry_b = re.sub('([BR])', '1', entry)
        entry_b = re.sub('([FL])', '0', entry_b)

        row = int(entry_b[:7], base=2)
        col = int(entry_b[7:], base=2)

        output.append((row, col))

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    max_id = -999

    for (row, col) in dataset:
        seat_id = row * 8 + col
        if seat_id > max_id:
            max_id = seat_id

    return max_id

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    seats = []

    for (row, col) in dataset:
        seat_id = row * 8 + col
        seats.append(seat_id)

    seats.sort()

    for index in range(1, len(seats) - 1):
        this_seat = seats[index]
        next_seat = seats[index + 1]

        if next_seat != this_seat + 1:
            my_seat = this_seat + 1

    return my_seat
