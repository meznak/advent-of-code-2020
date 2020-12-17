'''
Advent of Code Day 17
Conway Cubes
'''

from .cube import Cube

SAMPLE_SOLUTIONS = [112]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if item == '':
            continue
        output.append(list(item))

    return output

def count_neighbors(cubes: list, location: tuple) -> int:
    '''Count a cube's active neighbors'''
    count = 0

    for z in range(location[2] - 1, location[2] + 2):
        for y in range(location[1] - 1, location[1] + 2):
            for x in range(location[0] - 1, location[0] + 2):
                if (x, y, z) == location or (x, y, z) not in cubes:
                    continue
                if cubes[(x, y, z)]:
                    count += 1
    return count

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    cubes = {}

    # Set known boundaries of the grid
    min_x = 0
    max_x = len(dataset[0])
    min_y = 0
    max_y = len(dataset)
    min_z = 0
    max_z = 1

    # Generate initial cubes
    for y, item in enumerate(dataset):
        for x, char in enumerate(item):
            cubes[(x, y, 0)] = char == '#'

    for _ in range(6):
        changed_cubes = {}

        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    cube = (x, y, z)
                    neighbors = count_neighbors(cubes, cube)

                    if cube in cubes \
                        and cubes[cube] \
                        and neighbors not in [2,3]:
                        # If a cube is active and exactly 2 or 3 of its
                        # neighbors are also active, the cube remains active.
                        # Otherwise, the cube becomes inactive.
                        changed_cubes[cube] = False

                    elif (cube not in cubes \
                        or not cubes[cube]) \
                        and neighbors == 3:
                        # If a cube is inactive but exactly 3 of its neighbors
                        # are active, the cube becomes active. Otherwise, the
                        # cube remains inactive.
                        changed_cubes[cube] = True

                        # Extend grid boundaries, if needed.
                        min_x = min(min_x, x)
                        max_x = max(max_x, x)
                        min_y = min(min_y, y)
                        max_y = max(max_y, y)
                        min_z = min(min_z, z)
                        max_z = max(max_z, z)

        for cube in changed_cubes:
            cubes[cube] = changed_cubes[cube]

    return sum([cubes[cube] for cube in cubes])

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
