'''
Advent of Code Day 24
Lobby Layout
'''

from .tile import Tile

SAMPLE_SOLUTIONS = [10]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        line = []

        index = 0
        length = len(item)

        if item == '':
            continue

        while index < length:
            token = item[index]

            if token in ['e', 'w']:
                index += 1
            else:
                token = item[index : index + 2]
                index += 2

            line.append(token)

        output.append(line)

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    center = Tile()
    tile = center

    for item in dataset:
        for direction in item:
            if getattr(tile, direction) is None:
                setattr(tile, direction, Tile())

                # Set neighbor relations
                if direction == 'e':
                    tile.e.w = tile
                    if tile.ne:
                        tile.e.nw = tile.ne
                        if tile.ne.e:
                            tile.e.ne = tile.ne.e
                        if tile.ne.e.se:
                            tile.e.e = tile.ne.e.se

                elif direction == 'se':
                    tile.se.nw = tile
                elif direction == 'sw':
                    tile.sw.ne = tile
                elif direction == 'w':
                    tile.w.e = tile
                elif direction == 'nw':
                    tile.nw.se = tile
                elif direction == 'ne':
                    tile.ne.sw = tile


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
