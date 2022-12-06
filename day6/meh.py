import numpy as np

# Advent of Code 2022 Day 6

def check_str(str):
    for i in range(len(str)):
        if str.count(str[i]) > 1:
            return False
    return True

with open('day6/input') as f:
    data = f.read()

    # Parse data
    print('part-1')
    for i in range(len(data)-4):
        if check_str(data[i:i+4]):
            print(i+4)
            break
    
    print('part-2')
    for i in range(len(data)-14):
        if check_str(data[i:i+14]):
            print(i+14)
            break
            