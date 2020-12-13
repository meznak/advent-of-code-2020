'''
Advent of Code Day 13
Shuttle Search
'''

SAMPLE_SOLUTIONS = [295]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    output.append(int(dataset[0]))
    buses = dataset[1].split(',')
    output.append([int(bus_id) for bus_id in buses if bus_id != 'x'])

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    earliest = dataset[0]
    time = earliest
    buses = dataset[1]

    while True:
        for bus_id in buses:
            if time % bus_id == 0:
                time_delta = time - earliest
                return bus_id * time_delta
        time += 1

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
