'''
Advent of Code Day 14
Docking Data
'''

import re
from copy import deepcopy

SAMPLE_SOLUTIONS = [165, 208]

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

def expand_address(address: str, start_index: int) -> list:
    '''Expand a masked address, replacing X with both 0 and 1'''
    addresses = []

    new_address_1 = deepcopy(address)
    new_address_2 = deepcopy(address)

    changed = False

    for index, bit in enumerate(address[start_index:], start_index):
        if bit == 'X':
            new_address_1[index] = '0'
            new_address_2[index] = '1'

            temp = expand_address(new_address_1, index)
            [addresses.append(addr) for addr in temp]

            temp = expand_address(new_address_2, index)
            [addresses.append(addr) for addr in temp]

            changed = True
            break
    if not changed:
        addresses.append(address)

    return addresses

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

    memory = {}

    for item in dataset:
        address = item['address']

        if address:
            address = bin(int(address))[2:].zfill(36)
            masked_address = list(address)

            for index, bit in enumerate(mask):
                if bit == '0':
                    masked_address[index] = address[index]
                elif bit == '1':
                    masked_address[index] = '1'
                else:
                    masked_address[index] = 'X'

            for addr in expand_address(masked_address, 0):
                address = int(''.join(addr), 2)
                memory[address] = item['value']

        else:
            mask = item['value']

    total = 0
    for addr, value in memory.items():
        total += int(value, 2)

    return total