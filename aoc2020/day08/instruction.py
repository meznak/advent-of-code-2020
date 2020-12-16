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
