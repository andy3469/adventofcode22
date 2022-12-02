import numpy as np

# Advent of Code 2022 Day 2

with open("day2/input") as f:
    data = f.read().splitlines()
    print("part-1")
    rounds_1 = []
    for line in data:
        score = 0
        if line[2] == "X":
            score += 1
            if line[0] == "A":
                score += 3
            elif line[0] == "B":
                score += 0
            elif line[0] == "C":
                score += 6
        elif line[2] == "Y":
            score += 2
            if line[0] == "A":
                score += 6
            elif line[0] == "B":
                score += 3
            elif line[0] == "C":
                score += 0
        elif line[2] == "Z":
            score += 3
            if line[0] == "A":
                score += 0
            elif line[0] == "B":
                score += 6
            elif line[0] == "C":
                score += 3
        rounds_1.append(score)
    
    print(sum(rounds_1))

    print("part-2")
    rounds_2 = []
    for line in data:
        score = 0
        if line[2] == "X":
            score += 0
            if line[0] == "A":
                score += 3
            elif line[0] == "B":
                score += 1
            elif line[0] == "C":
                score += 2
        elif line[2] == "Y":
            score += 3
            if line[0] == "A":
                score += 1
            elif line[0] == "B":
                score += 2
            elif line[0] == "C":
                score += 3
        elif line[2] == "Z":
            score += 6
            if line[0] == "A":
                score += 2
            elif line[0] == "B":
                score += 3
            elif line[0] == "C":
                score += 1
        rounds_2.append(score)
    print(sum(rounds_2))