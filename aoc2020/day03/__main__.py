'''
Advent of Code Day 03
Toboggan Trajectory
'''

from ..shared import read_input, run_solvers

SAMPLE_SOLUTIONS = [7, 336]

def count_trees_1(rows: [str]) -> int:
    '''Solve part 1'''
    row_num = 0
    col_num = 0
    line_count = len(rows)
    line_length = len(rows[0])
    tree_count = 0
    checked = []

    while row_num < line_count - 1:
        # Move the cursor
        row_num += 1
        col_num += 3

        line = rows[row_num]

        line = list(line)
        pos = col_num % line_length

        if line[pos] == '#':
            tree_count += 1
            line[pos] = 'X'
        else:
            line[pos] = 'O'

        checked.append(''.join(line))

    return tree_count

def count_trees_2(rows: [str]) -> int:
    '''Solve part 2'''
    product = 1

    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        row_num = 0
        col = 0
        col_num = len(rows)
        line_length = len(rows[0])
        tree_count = 0
        checked = []

        while row_num < col_num - 1:
            # Move the cursor
            row_num += slope[1]
            col += slope[0]

            line = rows[row_num]

            line = list(line)
            pos = col % line_length

            if line[pos] == '#':
                tree_count += 1
                line[pos] = 'X'
            else:
                line[pos] = 'O'

            checked.append(''.join(line))

        product *= tree_count

    return product

if __name__ == '__main__':
    samples, data = read_input(__file__)

    run_solvers(samples, data, [count_trees_1, count_trees_2], SAMPLE_SOLUTIONS)
