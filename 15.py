# Euler Problem 15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

def moves(size):
    grid = [None] * (size+1)
    grid = [grid] * (size+1)

    #print(grid)

    for i in range(0,size):
        grid[i][size] = 1
        grid[size][i] = 1
        #print(grid)

    for i in range(size-1, -1, -1):
        for j in range(size-1, -1, -1):
            grid[i][j] = grid[i+1][j] + grid[i][j+1]
    return grid[i][j]

print(moves(20))
