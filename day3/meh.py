import numpy as np

# Advent of Code 2022 Day 3

with open("day3/input") as f:
    data = f.read().splitlines()
    backpacks = []
    print("part-1")
    sum = 0
    for line in data:
        backpack = [line[:int(len(line)/2)], line[int(len(line)/2):]]
        same = sorted(set.intersection(set(backpack[0]), set(backpack[1])))
        for item in same:
            if (ord(item) < 97):
                sum += ord(item) - 64 + 26
            else:
                sum += ord(item) - 96

        backpacks.append(backpack)
    print(backpacks)
    print(sum)

    print("part-2")
    group = []
    sum = 0
    for line in data:
        group.append(line)
        if len(group) == 3:
            same = sorted(set.intersection(set(group[0]), set(group[1]), set(group[2])))
            for item in same:
                if (ord(item) < 97):
                    sum += ord(item) - 64 + 26
                else:
                    sum += ord(item) - 96
            group = []
    print(sum)