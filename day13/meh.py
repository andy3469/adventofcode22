from math import prod
from functools import cmp_to_key
#Advent of code 2022 day 13

def compare_lists(lst1, lst2):
        # If the items are integers, compare them directly
        if isinstance(lst1, int) and isinstance(lst2, int):
            return lst1 - lst2
        # If the items are lists, recursively compare them
        elif isinstance(lst1, list) and isinstance(lst2, list):
            for i,j in zip(lst1, lst2):
                if (ret := compare_lists(i, j)) != 0:
                    return ret
            return compare_lists(len(lst1), len(lst2))
        # If the items are of different types (one is an integer and the other is a list),
        # convert the integer to a list and try again
        else:
            if isinstance(lst1, int):
                return compare_lists([lst1], lst2)
            elif isinstance(lst2, int):
                return compare_lists(lst1, [lst2])


with open('day13/input') as f:
    file = f.read().splitlines()
    packets = [
        eval(line)
        for line in file
        if len(line)
    ]


    right_order = []
    for i, (left, right) in enumerate(zip(packets[::2], packets[1::2])):
        if compare_lists(left,right) <=0:
            right_order.append(i+1)
    print(sum(right_order))

    keys = [[[2]], [[6]]]
    key_pkt = []
    for i, pkt in enumerate(sorted(packets + keys, key=cmp_to_key(compare_lists))):
        if pkt in keys:
            key_pkt.append(i+1)
    print(prod(key_pkt))
