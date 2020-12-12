'''
Advent of Code Day 11
Seating System
'''

from copy import deepcopy

SAMPLE_SOLUTIONS = [37]

class Cell(object):
    '''Stores info about a grid cell'''

    def __init__(self, is_seat: bool):
        self.is_seat = is_seat
        self.is_occupied = False

    def count_neighbors(self, x: int, y: int, grid: [int]) -> int:
        '''Count which of a cells neighbors are occupied seats'''

        # Determine grid boundaries
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        count = 0

        for row in range(y - 1, y + 2):
            # Check grid bounds
            if row >= 0 and 0 <= row <= max_y:
                for col in range(x - 1, x + 2):
                    # Check grid bounds and exclude self
                    if 0 <= col <= max_x \
                        and not (row == y and col == x):
                        if grid[row][col].is_seat and grid[row][col].is_occupied:
                            count += 1

        return count

    def __repr__(self):

        if self.is_occupied:
            char = '#'
        elif self.is_seat:
            char = 'L'
        else:
            char = '.'

        return char

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if item != '':
            row = []
            for cell in item:
                if cell == 'L':
                    is_seat = True
                else:
                    is_seat = False
                row.append(Cell(is_seat))
            output.append(row)

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    changed = True

    # Update seats until chaos stabilizes
    while changed:
        current_grid = deepcopy(dataset)
        changed = False

        for y, row in enumerate(dataset):
            for x, cell in enumerate(row):
                if cell.is_seat:
                    neighbors = cell.count_neighbors(x, y, current_grid)

                    if not cell.is_occupied and neighbors == 0:
                        cell.is_occupied = True
                        changed = True
                    elif cell.is_occupied and neighbors >= 4:
                        cell.is_occupied = False
                        changed = True

    # Count occupied seats
    occupied_seats = 0

    for row in dataset:
        for cell in row:
            if cell.is_occupied:
                occupied_seats += 1

    return occupied_seats

def solve_2(dataset: list) -> int:
    '''Solve part 2'''
    for item in dataset:
        # TODO: Build solution
        pass
