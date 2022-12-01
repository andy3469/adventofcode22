import numpy as np

# Parse text
with open('input1', 'r') as f:
    text = f.read()
    elf = []
    curr = []
    for line in text.split('\n'):
        if line == '':
            if len(curr) > 0:
                elf.append(curr)
                curr = []
        else:
            curr.append(int(line))
    print('part-1')
    print(max([sum(x) for x in elf]))
    print('part-2')
    print(sum(sorted([sum(x) for x in elf])[-3:]))