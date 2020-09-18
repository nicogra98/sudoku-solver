import os
import sys

"""
@Author Nicolas Granados
Solves a sudoku problem given by a file
ex: python sudoku-solver grid.txt
"""

"""
Function to print "nicely" the sudoku grid
"""
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
                print(str(grid[x][y]) + " ",end="")

"""
Function to check if its possible to put an n number in an x,y position
"""
def possible(x,y,n,grid):
    """
    We check rows
    """
    for i in range(0,9):
        if int(grid[i][y]) == n:
            return False
    
    """
    We check columns
    """
    for i in range(0,9):
        if int(grid[x][i]) == n:
            return False
    
    """
    We check the box
    """
    x_square = (x // 3) * 3
    y_square = (y // 3) * 3

    for i in range(x_square,x_square + 3):
        for j in range(y_square,y_square + 3):
            if int(grid[i][j]) == n:
                return False
    
    return True

"""
Function that solves the problem
"""
def solve(grid):
    for x in range(0,9):
        for y in range(0,9):
            if int(grid[x][y]) == 0: #we check if its an empty space
                for n in range(1,10): #we try every number possible
                    if possible(x,y,n,grid): 
                        grid[x][y] = n #if its possible then we put the number there
                        solve(grid)#we keep solving
                        grid[x][y] = 0 #we backtrack
                return
    print("Finished!")
    print_grid(grid)

if __name__ == "__main__":
file = open(os.getcwd() + "/" + sys.argv[1])

grid = file.read().split("\n")

for x in range(0,9):
    grid[x] = grid[x].split(" ")

print_grid(grid)
solve(grid)