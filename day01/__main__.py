import sys, os

def main(in_file):
    entries = []

    path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(path)

    with open(in_file, 'r') as f:
        lines = f.readlines()

    entries = [int(entry) for entry in lines]

    print(f'part 1: {solve_1(entries)}')
    print(f'part 2: {solve_2(entries)}')

def solve_1(entries):
    for i in range(len(entries)):
        for j in range(i, len(entries)):
            a = entries[i]
            b = entries[j]
            if a + b == 2020:
                    return a * b

def solve_2(entries):
    for i in range(len(entries)):
        for j in range(i, len(entries)):
            for k in range(j, len(entries)):
                a = entries[i]
                b = entries[j]
                c = entries[k]
                if a + b + c == 2020:
                        return a * b * c

if __name__ == "__main__":
    in_file = sys.argv[1]
    main(in_file)