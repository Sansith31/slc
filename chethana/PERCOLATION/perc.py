# Import necessary modules
from export import text_file, html
import random
import sys
from prettytable import PrettyTable as PT, ALL
# Initialize PrettyTable object for displaying the grid
table=PT()
table.hrules=ALL
status=''


# Function to obtain grid size from user input or default values
def get_size():
    try:
        if len(sys.argv) < 2:
            rows, columns = 5, 5  # Default size if no input provided
        else:
            perc=sys.argv[1].split('x')
            rows=int(perc[0])
            columns=int(perc[1])
            # Check if grid size is within specified range
            if not (3 <= rows <= 9 and 3 <= columns <= 9):
                print('Grid size out of range. Program will terminate!')
                exit()
    except ValueError:
        print('Invalid input. Program will terminate!')
        exit()
    return rows, columns

# Function to create the grid with random numbers and blank spaces
def create_table(rows,columns):
    # Creating an empty 2D list for the percolation process
    array = [[0 for i in range(columns)] for j in range(rows+1)]
    # Fill grid with random numbers and blank spaces
    for i in range(rows):
        for j in range(columns):
            rand=random.randrange(0,99)
            if len(str(rand))==1:
                array[i][j]='  '# If random number is single-digit, add blank spaces
            else:
                array[i][j]=rand
    # Add rows to PrettyTable for display
    for i in range(rows):
        table.add_row(array[i])
    print(table.get_string(header=False))
    return array

# Function to check percolation in the grid
def check_percolation(grid,rows,columns):
    global status       
    for j in range(columns):
        status = 'OK'
        for i in range(rows):
            if grid[i][j] == '  ':
                status = 'NO'# If blank space found in a column, percolation fails
                break
        grid[rows][j] = status# Record percolation status for each column
    for i in range(columns):
        print(f'  {grid[rows][i]}', end=' ')

# Main function to execute the program        
def main():
        dimension = get_size()
        grid=create_table(dimension[0],dimension[1])
        row,column=dimension[0],dimension[1]
        check_percolation(grid,row,column)
        time=text_file(grid)
        html(time,grid)
main()

