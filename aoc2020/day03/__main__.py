from ..shared import read_input
from typing import Callable

sample_solution_1 = 20

def count_trees_1(data: [str]) -> int:
    row = 0
    col = 0
    line_count = len(data)
    tree_count = 0

    while row < line_count:
        while data[row] == '':
            row += 1
        line = data[row]

        # Extend the current line as needed
        while col >= len(line) + 1:
            line += line

        if line[col] == '#':
            tree_count += 1

        # Move the cursor
        row += 1
        col += 3

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