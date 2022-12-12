from collections import deque
#Advent of code 2022 day 12

grid = []
data = []

def getNeighbors(grid, pos):
    neighbors = []
    potential = []
    i,j = pos
    height = grid[i][j]
    if i > 0:
        neighbors.append((i - 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if i < len(grid) - 1:
        neighbors.append((i + 1, j))
    if j < len(grid[0]) - 1:
        neighbors.append((i, j + 1))

    for neighbor in neighbors:
        pi,pj = neighbor
        if grid[pi][pj] - height <= 1:
            potential.append((pi,pj))
    return potential

    
def hike(grid, start, end):
    visited = set()
    visited.add(start)
    queue = deque()
    queue.append((start,0))
    while len(queue) > 0:
        (pos,d) = queue.popleft()

        neighbors = getNeighbors(grid, pos)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            if neighbor == end:
                return d+1
            else:
                visited.add(neighbor)
                queue.append((neighbor,d+1))
    
    return -1

with open('day12/input') as f:
    file = f.read()
    
    for line in file.splitlines():
        data.append([x for x in line.strip()])
        grid_line = []
        for c in line.strip():
            if c == 'S':
                start = (len(grid),len(grid_line))
                grid_line.append(0)
            elif c == 'E':
                end = (len(grid),len(grid_line))
                grid_line.append(25)
            else:
                h = ord(c) - ord('a')
                grid_line.append(h)
        grid.append(grid_line)

    print('part-1')
    print(start,end)
    print(hike(grid, start, end))

    print('part-2')
    hikes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                h = hike(grid,(i,j),end)
                if h > 0:
                    hikes.append(h)
    print(min(hikes))
    


    