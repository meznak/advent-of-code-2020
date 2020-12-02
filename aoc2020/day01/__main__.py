from  ..shared import read_input

sample_solution_1 = 514579
sample_solution_2 = 241861950

def solve_1(entries: [int]) -> int:
    for i in range(len(entries)):
        for j in range(i, len(entries)):
            a = entries[i]
            b = entries[j]
            if a + b == 2020:
                    return a * b

def solve_2(entries: [int]) -> int:
    for i in range(len(entries)):
        for j in range(i, len(entries)):
            for k in range(j, len(entries)):
                a = entries[i]
                b = entries[j]
                c = entries[k]
                if a + b + c == 2020:
                        return a * b * c

if __name__ == "__main__":
    sample, data = read_input(__file__)
    sample = [int(entry) for entry in sample]
    data = [int(entry) for entry in data]

    sample_result_1 = solve_1(sample)
    assert(sample_result_1 == sample_solution_1), \
        f'''Sample solution 1 incorrect:
        Expected {sample_solution_1}, received {sample_result_1}'''
    print(f'part 1: {solve_1(data)}')

    sample_result_2 = solve_2(sample)
    assert(sample_result_2 == sample_solution_2), \
        f'''Sample solution 2 incorrect:
        Expected {sample_solution_2}, received {sample_result_2}'''
    print(f'part 2: {solve_2(data)}')