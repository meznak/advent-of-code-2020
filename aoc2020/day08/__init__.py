'''
Advent of Code Day 08
Handheld Halting
'''

SAMPLE_SOLUTIONS = [5, 8]

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
        self.was_tried = False

    def interpret(self):
        '''Determine the result of an instruction'''
        instr_ptr = 1
        accumulator = 0

        if self.code == 'nop':
            pass
        elif self.code == 'acc':
            accumulator = self.value
        elif self.code == 'jmp':
            instr_ptr = self.value

        return instr_ptr, accumulator

    def flip(self):
        '''Swap a nop for jmp or vice versa'''

        if self.code == 'nop':
            self.was_tried = True
            self.code = 'jmp'
        elif self.code == 'jmp':
            self.was_tried = True
            self.code = 'nop'

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

    instr_ptr = 0
    accumulator = 0

    while program[instr_ptr].run_count == 0:
        instruction = program[instr_ptr]
        instruction.run_count += 1

        ip_delta, acc_delta = instruction.interpret()

        instr_ptr += ip_delta
        accumulator += acc_delta

    return accumulator

def solve_2(program: list) -> int:
    '''Solve part 2'''

    program_end = len(program)

    found = False
    while not found:
        changed_index = -1
        instr_ptr = 0
        accumulator = 0

        # Run the program
        while program[instr_ptr].run_count == 0:
            instruction = program[instr_ptr]
            instruction.run_count += 1

            if changed_index == -1 \
                and instruction.code in ['nop', 'jmp'] \
                and not instruction.was_tried:
                changed_index = instr_ptr
                instruction.flip()

            ip_delta, acc_delta = instruction.interpret()

            instr_ptr += ip_delta
            accumulator += acc_delta

            if instr_ptr >= program_end:
                found = True
                break

        if not found:
            program[changed_index].flip()
            for instruction in program:
                instruction.run_count = 0

    return accumulator
