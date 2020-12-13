'''
Advent of Code Day 13
Shuttle Search
'''

SAMPLE_SOLUTIONS = [295, 1068781]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = [-1, []]

    output[0] = int(dataset[0])
    buses = dataset[1].split(',')

    for bus_id in buses:
        if bus_id != 'x':
            output[1].append(int(bus_id))
        else:
            output[1].append(bus_id)

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    earliest = dataset[0]
    time = earliest
    # strip x from the list of buses
    buses = [bus_id for bus_id in dataset[1] if bus_id != 'x']

    while True:
        for bus_id in buses:
            if time % bus_id == 0:
                time_delta = time - earliest
                return bus_id * time_delta
        time += 1

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    buses = list(enumerate(dataset[1]))
    buses = [bus for bus in buses if bus[1] != 'x']

    if len(buses) > 10:
        earliest = 100000000000000
    else:
        earliest = 1000000
    time_step = max([bus[1] for bus in buses])

    for bus in buses:
        if bus[1] == time_step:
            offset = (earliest + bus[1]) % bus[1]
            start_time = earliest + 2 * bus[1] - offset - bus[0]
            break

    found = False

    while not found:
        for bus in buses:
            if (start_time + bus[0]) % bus[1] != 0:
                start_time += time_step
                break
            if bus == buses[-1]:
                found = True
                break

    return start_time
