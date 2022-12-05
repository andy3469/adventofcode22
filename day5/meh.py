import numpy as np

# Advent of Code 2022 Day 5

with open('day5/input') as f:
    s, moves = f.read().split('\n\n')

    # Parse crates
    lastline_len = len(s.splitlines()[-1].rstrip())

    crates = [[] for _ in range((lastline_len + 2) // 4)]

    for line in s.splitlines():
        for i, c in enumerate(line[1::4]):
            if not c.isspace():
                crates[i].append(c)

    for crate in crates:
        crate.reverse()
    crates_copy = [crate.copy() for crate in crates]

    print('part-1')
    for move in moves.splitlines():
        _, x, _, y, _, z = move.split()
        x = int(x)
        y = int(y)
        z = int(z)
        for _ in range(x):
            crates[z-1].append(crates[y-1].pop())
    print(''.join([crate[-1] if crate else '' for crate in crates]))

    print('part-2')
    crates = crates_copy
    for move in moves.splitlines():
        _, x, _, y, _, z = move.split()
        x = int(x)
        y = int(y)
        z = int(z)
        temp_crate = []
        for _ in range(x):
            temp_crate.append(crates[y-1].pop())
        for _ in range(x):
            crates[z-1].append(temp_crate.pop())

    print(''.join([crate[-1] if crate else '' for crate in crates]))
