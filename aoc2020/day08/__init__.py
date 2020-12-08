'''
Advent of Code Day 08
Handheld Halting
'''

SAMPLE_SOLUTIONS = [5]

class Instruction(object):
    '''A single instruction
    nop - No operation
    acc - Add value to accumulator
    jmp - jump to instruction at offset
    '''

    def __init__(self, code: str, value: int):
        self.code = code
        self.value = value
        self.run_count = 0

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if len(item) != 0:
            code, value = tuple(item.split(' '))
            instruction = Instruction(code, int(value))
            output.append(instruction)

    return output

def solve_1(program: list) -> int:
    '''Solve part 1'''

    ip = 0
    acc = 0

    while program[ip].run_count == 0:
        code = program[ip].code
        value = program[ip].value
        program[ip].run_count += 1

        if code == 'nop':
            pass
        elif code == 'acc':
            acc += value
        elif code == 'jmp':
            ip += value

        if code != 'jmp':
            ip += 1

    return acc

def solve_2(dataset: list) -> int:
    '''Solve part 2'''
    for item in dataset:
        # TODO: Build solution
        pass
