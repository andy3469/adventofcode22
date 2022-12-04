import numpy as np

# Advent of Code 2022 Day 4

with open("day4/input") as f:
    data = f.read().splitlines()
    sections = []
    for line in data:
        sec = []
        paires = line.split(",")
        for p in paires:
            section = p.split("-")
            
            sec.append([int(num, base=10) for num in section])
        sections.append(sec)
    print("part-1")
    sum = 0
    for section in sections:
        if (section[0][0] <= section[1][0] and section[0][1] >= section[1][1]) or (section[0][0] >= section[1][0] and section[0][1] <= section[1][1]):
            sum += 1
    print(sum)

    print("part-2")
    sum = 0
    for section in sections:
        sec1 = np.arange(section[0][0], section[0][1]+1)
        sec2 = np.arange(section[1][0], section[1][1]+1)
        same = sorted(set.intersection(set(sec1), set(sec2)))
        if len(same) > 0:
            sum += 1
    print(sum)
