import sys

#
# CIS 500, Fall 2021, Project 2 - Game of Life
#

#
# Funtion that reads the contents of a given file, creates, and
# returns the initial grid (as a list of lists) for the game. The
# file contains just a single line of values.
# 
# You can assume that the contents of the file adhere to the following
# format conventions:
#   - File contains only integers
#   - The first number is the length (rows) of the grid
#   - The second number is the width (columns) of the grid
#   - The remaining values are only 0s and 1s indicating if a cell is dead or live
#   - After the first two numbers, there will be rows * columns number of values
#     (values of first row followed by values of second row and so on)
# 
def create_grid_from_file(filename):
    myfile = open(filename,"r")
    
    rows = 0 
    cols = 0
    grid = []
    for i in myfile:
        rows = int(i[0])
        cols = int(i[2])
        j = i[4:].split(" ")
        for x in range(rows):
            grid1 = []
            for y in range(cols):
                if (j[rows*x + y]) == "1":
                    grid1.append(1)
                else: 
                    grid1.append(0)
            grid.append(grid1)
    #print(grid)
    
    myfile.close()
    return grid

#create_grid_from_file("beacon.txt")
    
  
    
# Function that saves the current state of a grid to the file specified
# following the file format conventions described above (also in the project specifications).
#
def save_grid_to_file(filename, grid):
   myfile = open(filename, "w")
   rows = len(grid)
   columns = len(grid[0])
   
   myfile.write(str(rows) + " " + str(columns))
   
   for i in range(len(grid)):
       for j in range(len(grid[0])):
           myfile.write(" "+str(grid[i][j]))
       
   myfile.close()
       
                    
   
    

#
# Function that returns the grid contents as a string in the format specified below
# as demonstrated using an example grid:
#
#   Example input grid: [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
#   String returned: '. . . . .\n. . X . .\n. . X . .\n. . X . .\n. . . . .'
#
#   Make sure to strip off any leading and trailing whitespace before the string is returned.
#
def grid_as_string(grid):
    x = " "
    for j in range(len(grid)):
        for i in range(len(grid[j])-1):
            if grid[j][i] == 1:
                x+="X "
            else: 
                x+=". "
        if grid[j][-1] == 1: 
            x+="X\n"
        else: 
            x+=".\n"
    return x.strip()
        

#
# Function that makes a deep copy of the given grid and returns it.
#
def copy_grid(grid):
    grid1 = []
    
    for x in range(len(grid)):
        grid2 =[]
        for y in range(len(grid[x])):
            grid2.append(grid[x][y])
        grid1.append(grid2)
    return grid1
#
# Function that mutates the given grid and returns the result as a new grid.
# It does not alter the input grid. It makes a copy (using copy_grid function)
# of the input grid, advances it to next generation by making appropriate changes,
# and returns the new grid.
#
def mutate_grid(grid):
    new_grid = copy_grid(grid)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            neighbors = get_nbr_of_neighbors(row, col, grid)
            if grid[row][col] and neighbors in (2, 3):
                    new_grid[row][col] = 1
            elif not grid[row][col] and neighbors == 3:
                    new_grid[row][col] = 1
            else:
                new_grid[row][col] = 0
    return(new_grid)
   


#
# Function that returns the number of live neighbors of a cell at
# position [row,col] in the grid.
#
def get_nbr_of_neighbors(row,col,grid):
    neighbors = 0
    for r in range(row - 1, row + 2): 
        for c in range(col - 1, col + 2):
            if not (c == col and r == row):
                try: 
                    neighbors += grid[r][c]
                except IndexError:
                    continue
    return neighbors 

# Driver to play the game from command line.
#
def main():
    if len(sys.argv) != 2:
        print('Usage error - This program requires a filename as argument')
        print('Correct usage: python project2.py filename')
        print('Example: python project2.py beacon.txt')
        sys.exit()
    grid = create_grid_from_file(sys.argv[1])
    print(grid_as_string(grid) + '\n')
    while(True):
        response = input('Press q to quit, n to iterate, w to save to file, or any other key to move to next generation: ')
        response = response.upper()
        if response == 'Q':
            print('Exiting the program.')
            sys.exit()
        elif response == 'W':
            filename = input('Enter a filename to save the grid to: ')
            save_grid_to_file(filename,grid)
            print('Grid saved to file %s' % filename)
        elif response == 'N':
            nbr = int(input('How any iterations? '))
            for i in range(nbr):
                grid = mutate_grid(grid)
                print(grid_as_string(grid) + '\n')
        else:
            grid = mutate_grid(grid)
            print(grid_as_string(grid) + '\n')


# run main to play the game if this script is executed as a top-level program
if __name__ == '__main__':
    main()
