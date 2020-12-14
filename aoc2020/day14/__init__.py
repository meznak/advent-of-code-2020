'''
Advent of Code Day 14
Docking Data
'''

import re
from copy import deepcopy

SAMPLE_SOLUTIONS = [165]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    re_addr_pat = re.compile(r'mem\[(?P<addr>\d+)')

    output = []

    for item in dataset:
        if item != '':
            line = item.split(' = ')
            if line[0] == 'mask':
                address = None
                value = line[1]
            else:
                address = re_addr_pat.search(item)
                address = address.groupdict()['addr']
                address = int(address)

                value = bin(int(line[1]))[2:].zfill(36)

            instruction = {}
            instruction['address'] = address
            instruction['value'] = value

            output.append(instruction)

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    memory = [None] * 65535

    for item in dataset:
        address = item['address']
        if address:
            new_mem = ['0'] * 36
            value = item['value']

            for index, bit in enumerate(mask):
                if bit  ==  '0':
                    new_mem[index] = '0'
                elif bit == '1':
                    new_mem[index] = '1'
                else:
                    new_mem[index] = value[index]

            memory[address] = ''.join(new_mem)
        else:
            mask = item['value']

    total = 0
    for value in memory:
        if value:
            value = int(value, 2)
            total += value

    return total

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
