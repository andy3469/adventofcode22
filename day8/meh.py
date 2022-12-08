
#Advent of Code 2022 Day 8

def is_visible(grid, i, j):
    # Check visibility from the left
    for k in range(j):
        if grid[i][k] >= grid[i][j]:
            break
    else:
        return True

    # Check visibility from the right
    for k in range(j+1, len(grid[i])):
        if grid[i][k] >= grid[i][j]:
            break
    else:
        return True

    # Check visibility from the top
    for k in range(i):
        if grid[k][j] >= grid[i][j]:
            break
    else:
        return True

    # Check visibility from the bottom
    for k in range(i+1, len(grid)):
        if grid[k][j] >= grid[i][j]:
            break
    else:
        return True

# Function to determine the scenic score for a tree at a given position


# Function to determine the scenic score for a tree at a given position
def scenic_score(grid, i, j):
  # Function to compute the viewing distance in a given direction
    tree_height = grid[i][j]
    up_distance = 0
    down_distance = 0
    left_distance = 0
    right_distance = 0

    # Up direction
    for k in range(i-1, -1, -1):
        up_distance += 1
        if grid[k][j] >= tree_height:
            break

    # Down direction
    for k in range(i+1, len(grid)):
        down_distance += 1
        if grid[k][j] >= tree_height:
            break

    # Left direction
    for k in range(j-1, -1, -1):
        left_distance += 1
        if grid[i][k] >= tree_height:
            break

    # Right direction
    for k in range(j+1, len(grid[i])):
        right_distance += 1
        if grid[i][k] >= tree_height:
            break



    return up_distance * down_distance * left_distance * right_distance



# Parse the input into a grid of integers
grid = []
with open("day8/input") as f:
    for line in f:
        grid.append([int(x) for x in line.strip()])

print('part-1')
# Count the number of visible trees
visible_trees = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if is_visible(grid, i, j):
            visible_trees += 1


print(visible_trees)

print('part-2')
# Compute the scenic score for each tree and keep track of the maximum
max_score = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        score = scenic_score(grid, i, j)
        if score > max_score:
            max_score = score

# Print the result
print(max_score)
