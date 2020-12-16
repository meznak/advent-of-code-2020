'''
Advent of Code Day 16
Ticket Translation
'''

import re
from copy import copy

SAMPLE_SOLUTIONS = [71, 156]

def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []
    fields = {}
    tickets = []
    section = 0

    re_fields = re.compile(r'(?P<name>[^:]+): (?P<min1>\d+)-(?P<max1>\d+) or (?P<min2>\d+)-(?P<max2>\d+)')

    for item in dataset:
        if item == '':
            section += 1
        elif item in ['your ticket:', 'nearby tickets:']:
            continue
        elif section == 0:
            # fields
            name, min1, max1, min2, max2 = re_fields.search(item).groups()
            fields[name] = [int(min1), int(max1), int(min2), int(max2)]
        elif section == 1:
            # your ticket
            output.append([int(number) for number in item.split(',')])
        else:
            # nearby tickets
            tickets.append([int(number) for number in item.split(',')])

    output.append(fields)
    output.append(tickets)

    return output

def invalidate_tickets(fields: dict, tickets: list) -> list:
    '''Checks for invalid values.
    Returns list of invalid ticket indices and values.'''

    invalid_tickets = []

    for ticket in tickets:
        for number in ticket:
            valid = False

            for field in fields:
                if fields[field][0] <= number <= fields[field][1] \
                    or fields[field][2] <= number <= fields[field][3]:
                    valid = True
                    break

            if not valid:
                invalid_tickets.append((ticket, number))

    return invalid_tickets

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    fields = dataset[1]
    tickets = dataset[2]

    invalid_tickets = invalidate_tickets(fields, tickets)
    error_rate = sum([ticket[1] for ticket in invalid_tickets])

    return error_rate

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    my_ticket = dataset[0]
    fields = dataset[1]
    tickets = dataset[2]

    field_order = [[copy(field) for field in fields] for field in fields]

    # Remove known bad tickets
    invalid_tickets = invalidate_tickets(fields, tickets)
    for ticket in invalid_tickets:
        tickets.remove(ticket[0])

    # Determine field order
    for ticket in tickets:
        for index, number in enumerate(ticket):
            for field in fields:
                if not (fields[field][0] <= number <= fields[field][1] \
                    or fields[field][2] <= number <= fields[field][3]):
                    field_order[index].remove(field)

    # Remove known fields from possibility list of others
    changed = True
    while changed:
        changed = False
        for field in field_order:
            if len(field) == 1:
                field_name = field[0]
                for other_field in field_order:
                    if other_field == field:
                        continue

                    try:
                        other_field.remove(field_name)
                        changed = True
                    except ValueError:
                        pass

    # Find fields starting with 'departure'
    product = 1
    for index, field in enumerate(field_order):
        if field[0][:9] == 'departure':
            product *= my_ticket[index]

    return product
