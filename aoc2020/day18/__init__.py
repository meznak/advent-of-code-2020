'''
Advent of Code Day 18
Operation Order
'''

SAMPLE_SOLUTIONS = [148, 328]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if item != '':
            item = ''.join(item.split(' '))
            output.append(item)

    return output

def calculate(expression: str, depth = 0) -> int:
    '''Calculate expressions without operator precedence'''
    value = 0
    operator = '+'

    index = 0
    end = len(expression)

    while index < end:
        char = expression[index]
        if char in ['+', '*']:
            operator = char
            index += 1
            continue

        if char == '(':
            term, offset = calculate(expression[index + 1:], depth + 1)
            index += offset
        elif char == ')':
            index += 1
            break
        else:
            term = int(char)

        if operator == '+':
            value += term
        elif operator == '*':
            value *= term

        index += 1

    return value, index

def calculate_add_first(expression: str, depth = 0) -> int:
    '''Calculate an expression, giving addition precedence
        #newmath'''

    value = 0
    operator = '+'

    index = 0
    end = len(expression)

    while index < end:
        char = expression[index]
        if char == '*':
            operator = '*'
            index += 1
            continue
        if char == '+':
            operator = '+'

            term, offset = calculate_add_first(expression[index + 1:], depth)
            index += offset + 1

        if char == '(':
            term, offset = calculate_add_first(expression[index + 1:], depth + 1)
            index += offset
        elif char == ')':
            index += 1
            break
        else:
            term = int(char)

        if operator == '+':
            value += term
        elif operator == '*':
            value *= term

        index += 1

    return value, index

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    total = 0

    for item in dataset:
        total += calculate(item)[0]

    return total

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    total = 0

    for item in dataset:
        total += calculate_add_first(item)[0]

    return total
