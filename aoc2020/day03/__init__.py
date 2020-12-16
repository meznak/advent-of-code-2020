'''
Advent of Code Day 03
Toboggan Trajectory
'''

SAMPLE_SOLUTIONS = [7, 336]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = [line for line in dataset if line != '']

    # Nothing to parse
    return output

def solve_1(rows: [str]) -> int:
    '''Solve part 1'''
    row_num = 0
    col_num = 0
    line_count = len(rows)
    line_length = len(rows[0])
    tree_count = 0

    while row_num < line_count - 1:
        # Move the cursor
        row_num += 1
        col_num += 3

        line = rows[row_num]

        pos = col_num % line_length

        if line[pos] == '#':
            tree_count += 1

    return tree_count

def solve_2(rows: [str]) -> int:
    '''Solve part 2'''
    product = 1

    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        row_num = 0
        col = 0
        col_num = len(rows)
        line_length = len(rows[0])
        tree_count = 0

        while row_num < col_num - 1:
            # Move the cursor
            row_num += slope[1]
            col += slope[0]

            line = rows[row_num]

            pos = col % line_length

            if line[pos] == '#':
                tree_count += 1

        product *= tree_count

    return product
