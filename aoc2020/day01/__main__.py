'''
Advent of Code Day 01
Report Repair
'''

from  ..shared import read_input, run_solvers

SAMPLE_SOLUTIONS = [514579, 241861950]

def solve_1(entries: [int]) -> int:
    '''Solve part 1'''

    for i in range(len(entries)):
        for j in range(i, len(entries)):
            a = entries[i]
            b = entries[j]
            if a + b == 2020:
                return a * b

def solve_2(entries: [int]) -> int:
    '''Solve part 2'''

    for i in range(len(entries)):
        for j in range(i, len(entries)):
            for k in range(j, len(entries)):
                a = entries[i]
                b = entries[j]
                c = entries[k]
                if a + b + c == 2020:
                    return a * b * c

if __name__ == "__main__":
    samples, data = read_input(__file__)
    samples_parsed = [[int(entry) for entry in sample] for sample in samples]
    data_parsed = [int(entry) for entry in data]

    solvers = [solve_1, solve_2]

    run_solvers(samples_parsed, data_parsed, solvers, SAMPLE_SOLUTIONS)
