# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    row = 0 #starting from 0 not 1
    square = "" #empty string

    while row < n:
        if row == 0 or row == n - 1: 
            square += "*" * n  #full row for top and bottom

        else:
            square += "*" + " " * (n - 2) + "*"  #hollow middle rows

        if row < n - 1:
            square += "\n"

        row += 1

    return square

# 1
# 12
# 123
# 1234
def number_pattern(n):
    row = 1
    np = "" #short for number pattern

    while row <= n:

        col = 1

        while col <= row:
            np += str(col)
            col += 1

        if row < n:
            np += "\n"
        row += 1

    return np


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0 #nothing has been added yet
    count = 1 #starts the count at 1 then goes up by one each time repeated through the while loop

    while count <= n:
        total += count #adds the number count represents at the time
        count += 1 #increases the number of count by 1

    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    row = 0 #starts from row 0 to not mess up the arithmatic
    pyramid = "" #empty string

    while row < n:
        pyramid += " " * (n - row - 1) + "*" * (2 * row  + 1) + "\n"
        row += 1

    return pyramid.rstrip()