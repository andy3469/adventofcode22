import re

#Advent of Code 2022 Day 15

def calc_mahattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


with open('day15/input') as f:
    lines = f.readlines()
    sensors = sorted([[*map(int, re.findall(r"-?\d+", line))] for line in lines])
    min_sx = min(x for x,_,_,_ in sensors)-1000000
    max_sx = max(x for x,_,_,_ in sensors)+1000000
    print(min_sx, max_sx)
    y = 2000000

    print('part-1')
    
    not_bcn = 0

    for x in range(min_sx,max_sx): #x parse x range on a given y value
        print('X = '+str(x)+' and not_bcn = '+str(not_bcn), end='\r')
        for sx,sy,bx,by in sensors:
            if calc_mahattan_distance(sx,sy,bx,by) >= calc_mahattan_distance(sx,sy,x,y) and (bx != x or by != y):
                not_bcn += 1
                break
    print("\r")
    print(not_bcn)

    print('part-2')

    for y in range(4000001):
        x = 0
        for sx,sy,bx,by in sensors:
            print('X = '+str(x)+' Y = '+str(y), end='\r')
            if calc_mahattan_distance(sx,sy,bx,by) >= calc_mahattan_distance(sx,sy,x,y):
                x = sx + calc_mahattan_distance(sx,sy,bx,by) - abs(sy - y) + 1
        if x <= 4000000:
            print(x,y)
            print(x * 4000000 + y)

    

