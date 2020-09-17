import os
import sys

def print_grid(grid):
    for x in range(0,9):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - -")

        for y in range(0,9):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")
            
            if y == 8:
                print(grid[x][y])
            else:
                print(grid[x][y] + " ",end="")


file = open(os.getcwd() + "/" + sys.argv[1])

grid = file.read().split("\n")

for x in range(0,9):
    grid[x] = grid[x].split(" ")

print_grid(grid)



