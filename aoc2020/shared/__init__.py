import os

def read_input(script_file: str) -> ([int], [int]):
    path = os.path.dirname(os.path.realpath(script_file))

    with open(os.path.join(path, 'sample'), 'r') as f:
        sample = [int(entry) for entry in f.readlines()]

    with open(os.path.join(path, 'input'), 'r') as f:
        data = [int(entry) for entry in f.readlines()]

    return (sample, data)