#!/bin/env python3

import sys, os

def main(in_file):
    entries = []

    path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(path)

    with open(in_file, 'r') as f:
        lines = f.readlines()

    entries = [int(entry) for entry in lines]

    print(check_nums(entries))

def check_nums(entries):
    for i in range(len(entries)):
        for j in range(i, len(entries)):
            for k in range(j, len(entries)):
                a = entries[i]
                b = entries[j]
                c = entries[k]
                if a + b + c == 2020:
                        return a * b * c

if __name__ == "__main__":
    in_file = sys.argv[1]
    main(in_file)