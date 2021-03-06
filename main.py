from time import perf_counter
from functools import reduce

import const
import solve


def printrow(row, table):
    """
    Prints a series of nine elements from a list

    Arguments:
        row : int : which series of element to print
        table : list : list of elements to print
    """
    text = ''
    for i in range(9*row, 9*row+9):
        digit = str(table[i].get_value())
        if digit == '0':
            digit = ' '
        text += digit
    print(text)


def printwhole(table):
    """
    Prints whole list in form of a 9x9 array

    Arguments:
        table : list : list of elements to print
    """
    for i in range(9):
        printrow(i, table)


def end_check(table):
    """
    Checks if all cells in the table are properly solved
    """
    return reduce(lambda x, y: x+y.get_value(), table, 0) == 405


if __name__ == "__main__":
    table = const.construct()
    print('----')
    start = perf_counter()  # Time measurement starts
    cases = solve.env(table)
    solve.layer_solve(cases)
    stop = perf_counter()
    print('----')
    printwhole(table)
    print('----')
    print((not end_check(table))*"not", 'solved in',
          str(round(stop-start, 3)), 'seconds')
