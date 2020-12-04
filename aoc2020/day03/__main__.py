from ..shared import read_input
from typing import Callable

sample_solution_1 = 7

def count_trees_1(data: [str]) -> int:
    row = 0
    col = 0
    line_count = len(data)
    line_length = len(data[0])
    tree_count = 0
    checked = []

    while row < line_count - 1:
        # Move the cursor
        row += 1
        col += 3

        line = data[row]

        line = list(line)
        pos = col % line_length

        if line[pos] == '#':
            tree_count += 1
            line[pos] = 'X'
        else:
            line[pos] = 'O'

        checked.append(''.join(line))

    return tree_count

def check_list(sample: [str], data: [str], count_trees: Callable[[list], int], sample_solution: int) -> int:
    run_count = 0

    for dataset in [sample, data]:
        tree_count = count_trees(dataset)

        if run_count == 0:
            assert(tree_count == sample_solution), \
                f'''Expected {sample_solution}, got {tree_count}'''
            run_count += 1
        else:
            return tree_count

if __name__ == '__main__':
    sample, data = read_input(__file__)

    tree_count = check_list(sample, data, count_trees_1, sample_solution_1)
    print(f'part 1: {tree_count}')