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
        self.neighbors = None

    def count_neighbors(self) -> int:
        '''Count which of a cells neighbors are occupied seats'''

        for neighbor in self.neighbors:
            if neighbor.is_occupied:
                count += 1

        return count

    def find_neighbors(self, x: int, y: int, grid: [int], \
        immediate: bool) -> None:
        '''Find first visible neighbor in each direction'''

        max_y = len(grid) - 1
        max_x = len(grid[0]) - 1

        offset = 1

        reached_edge = [False] * 8

        self.neighbors = [None] * max_x

        while True:
            # Directional offsets
            nw_pos = (y + offset * -1, x + offset * -1)
            n_pos = (y + offset * -1, 0)
            ne_pos = (y + offset * -1, x + offset)
            e_pos = (0, x + offset)
            se_pos = (y + offset, x + offset)
            s_pos = (y + offset, 0)
            sw_pos = (y + offset, x + offset * -1)
            w_pos = (0, x + offset * -1)

            directions = [nw_pos, n_pos, ne_pos, e_pos, se_pos, s_pos, sw_pos, w_pos]

            for index, position in enumerate(directions):
                # Skip if we've found this direction's neighbor or reached
                # the edge
                if self.neighbors[index] is None and not reached_edge[index]:
                    # Make sure we're looking within the grid
                    if 0 <= position[0] <= max_y and 0 <= position[1] <= max_x:
                        if grid[position[0]][position[1]].is_seat:
                            self.neighbors[index] = grid[position[0]][position[1]]
                    else:
                        reached_edge[index] = True

            # Stop looking if only asked for immediate neighbors, all edges
            # have been reached, or all neighbors have been found
            if immediate or sum(reached_edge) == 8 \
                or None not in self.neighbors:
                break

            offset += 1

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
                    neighbors = cell.count_neighbors(x, y, current_grid, True)

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
