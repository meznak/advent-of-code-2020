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
        self.new_state = False
        self.neighbors = None

    def count_neighbors(self) -> int:
        '''Count which of a cells neighbors are occupied seats'''

        count = 0

        for neighbor in self.neighbors:
            if neighbor and neighbor.is_occupied:
                count += 1

        return count

    def find_neighbors(self, x: int, y: int, grid: [int], \
        immediate: bool) -> None:
        '''Find first visible neighbor in each direction'''

        max_y = len(grid) - 1
        max_x = len(grid[0]) - 1

        offset = 1

        stop_search = [False] * 8

        self.neighbors = [None] * 8

        while True:
            # Directional offsets
            nw_pos = (y + offset * -1, x + offset * -1)
            n_pos = (y + offset * -1, x)
            ne_pos = (y + offset * -1, x + offset)
            e_pos = (y, x + offset)
            se_pos = (y + offset, x + offset)
            s_pos = (y + offset, x)
            sw_pos = (y + offset, x + offset * -1)
            w_pos = (y, x + offset * -1)

            directions = [nw_pos, n_pos, ne_pos, e_pos, se_pos, s_pos, sw_pos, w_pos]

            for index, position in enumerate(directions):
                # Skip if we've found this direction's neighbor or reached
                # the edge
                if self.neighbors[index] is None and not stop_search[index]:
                    # Make sure we're looking within the grid
                    if 0 <= position[0] <= max_y and 0 <= position[1] <= max_x:
                        if grid[position[0]][position[1]].is_seat:
                            self.neighbors[index] = grid[position[0]][position[1]]
                            stop_search[index] = True
                    else:
                        stop_search[index] = True

            # Stop looking if only asked for immediate neighbors, all edges
            # have been reached, or all neighbors have been found
            if immediate or sum(stop_search) == 8 \
                or None not in self.neighbors:
                break

            offset += 1

    @staticmethod
    def update_grid(dataset: list) -> list:
        '''Update seats until chaos stabilizes'''
        changed = True

        while changed:
            changed = False

            for y, row in enumerate(dataset):
                for x, cell in enumerate(row):
                    if cell.is_seat:
                        neighbors = cell.count_neighbors()

                        if not cell.is_occupied and neighbors == 0:
                            cell.new_state = True
                            changed = True
                        elif cell.is_occupied and neighbors >= 4:
                            cell.new_state = False
                            changed = True

            for row in dataset:
                for cell in row:
                    cell.is_occupied = cell.new_state

        return dataset

    @staticmethod
    def count_occupied_seats(dataset: list) -> int:
        '''Count occupied seats'''
        occupied_seats = 0

        for row in dataset:
            for cell in row:
                if cell.is_occupied:
                    occupied_seats += 1

        return occupied_seats

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

    for y, row in enumerate(dataset):
        for x, cell in enumerate(row):
            cell.find_neighbors(x, y, dataset, True)

    dataset = Cell.update_grid(dataset)

    return Cell.count_occupied_seats(dataset)

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
