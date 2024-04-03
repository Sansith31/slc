#importing needed modules
import random as rn
from prettytable import PrettyTable, ALL
import sys
from module import export_list

#declaring a function for getting user input and generating the grid
def grid_generate():
    try:
        matrix_size = sys.argv[1]
        if len(matrix_size)<=2 :
            exit()
        matrix_size = matrix_size.split("x")
        column = int(matrix_size[0])
        row = int(matrix_size[1])
    #making the program run the default 5x5 if a argument is not given
    except IndexError:
        column = 5
        row = 5
    except:
        print("invalid input, applicable argument(3x3, 9x9)")
        exit()
    if column > 9 or row > 9 or column < 3 or row < 3:
        print("Matrix size out of range, applicable argument(3x3, 9x9)")
        exit()
    else:
        pass

    #iniatializing a nested list 
    array = [[" " for _ in range(row)] for _ in range(column)]

    for j in range(column): 
        for i in range(row):
            rand_x = rn.randrange(8)
            rand_y = rn.randrange(8)
            #inserting a blank space if 2 randoms values are the same 
            if rand_x == rand_y:
                temp = "  "
                array[j][i] = temp
            #if the 2 random values are not same it will insert a number from 10 to 99 to the grid
            else:
                temp = rn.randint(10, 99)
                array[j][i] = temp
    return array

#declaring a function for checking percolation 
def check_perco(array):
    global check_list
    check_list = []
    for i in range(len(array[0])):
        column = []
        for j in range(len(array)):
            value = array[j][i]
            column.append(value)
        #appending NO if theres a blank space in a row
        if "  " in column:
            check_list.append("NO")
        #appending OK if theres not any blank space in a row
        if "  " not in column:
            check_list.append("OK")
    return check_list

#declaring a function for displaying both grid and list used to check percolation 
def display_list(array):
    global check_list
    table = array
    #calling the prettytable function for the table 
    table = PrettyTable()
    table.hrules = ALL
    table.header = False
    for i in array:
        table.add_row(i)
    print(table)
    for i in check_list:
        print(" ", i, end=" ")
    print("\r")

#declaring a function for calling other functions with the appropriate arguments 
def main():
    #calling the grid_generate function and intializing a variable with the return of the function 
    x = grid_generate()
    #calling the check_perco function and intializing a variable with the return of the function
    y = check_perco(x)
    #calling the display_list function and giving it the appropriate argument
    display_list(x)
    #calling the export_list function and giving it the appropriate arguments
    export_list(x, y)

#calling the main function 
main()  