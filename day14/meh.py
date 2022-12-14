#Advent of Code 2022 Day 14

def solve(grid):
    while True:
        sandx = 500
        sandy = 0
        while sandy+1 < len(grid):
            for x in (0, -1, 1):
                if grid[sandy+1][sandx+x] == '.':
                    sandy += 1
                    sandx += x
                    break
            else:
                grid[sandy][sandx] = 'o'
                break
        if sandy+1 >= len(grid) or grid[0][500] == 'o':
            return sum(1 for row in grid for c in row if c == 'o')



with open('day14/input') as f:
    rocks = [[list(map(int, pos.split(','))) for pos in l.strip().split(" -> ")] for l in f.readlines()]
    width = max(max(x for x, y in rock) for rock in rocks) + 200
    height = max(max(y for x, y in rock) for rock in rocks) + 1


    print('part-1')
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for rock in rocks:
        for (x1, y1), (x2, y2) in zip(rock, rock[1:]):
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[y][x] = '#'

    print(solve(grid))

    print('part-2')
    grid = [['.' for _ in range(width)] for _ in range(height+2)]
    for x in range(width):
        grid[height+1][x] = '#'
    for rock in rocks:
        for (x1, y1), (x2, y2) in zip(rock, rock[1:]):
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[y][x] = '#'
    print(solve(grid))

            