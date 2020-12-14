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

def egcd(a: int, b: int) -> tuple:
    '''Extended Euclidean GCD'''

    s1, s2, t1, t2 = 1, 0, 0, 1
    q, r = a // b, a % b
    s3 = s1 - q * s2
    t3 = t1 - q * t2
    while r:
        a, b = b, r
        s1, s2 = s2, s3
        t1, t2 = t2, t3

        q, r = a // b, a % b
        s3 = s1 - q * s2
        t3 = t1 - q * t2
    return b, s2, t2

def chinese_remainder(n_list: int, a_list: int) -> int:
    '''Chinese Remainder Theorem'''
    solution = 0
    N = 1

    for n in n_list:
        N *= n

    for n, a in zip(n_list, a_list):
        if n > 0:

            m = N // n
            gcd, x, y = egcd(n, m)

            solution += a * m * y

    return N - (solution % N)

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

    bus_ids = [bus[1] for bus in buses]
    offsets = [bus[0] for bus in buses]

    start_time = chinese_remainder(bus_ids, offsets)

    return start_time
