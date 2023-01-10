# File: Spiral.py

# Description:

# Student Name: Sneha Kamal

# Student UT EID: sk52223

# Course Name: CS 313E

# Unique Number: 52520

# Date Created: 08/31/2022

# Date Last Modified: 09/07/2022

# Input: n is an odd integer between 1 and 100

# Output: returns a 2-D list representing a spiral if n is even add one to n
import sys


def create_spiral(n):

    # adds 1 to n if its even
    if n % 2 == 0:
        n += 1
    spiral = [[0 for i in range(n)] for j in range(n)]

    direc = 1
    curr_x = n - 1
    curr_y = 0
    x_change = -1
    y_change = -1
    tl_corner = n**2 - (n-1)
    bl_corner = tl_corner - (n-1)
    br_corner = bl_corner - (n-1)

    # makes spiral
    for x in range(n * n):

        # starts from top right corner, goes backwards
        spiral[curr_y][curr_x] = n**2 - x

        # changes direction if at end of row or column or if next cell is filled
        if (n**2 - x == tl_corner) or\
            (n**2 - x == bl_corner) or\
            (n**2 - x == br_corner) or spiral[curr_y + y_change][curr_x + x_change] != 0:
            direc += 1

        # left
        if direc % 4 == 1:
           x_change = -1
           y_change = 0

        # down
        elif direc % 4 == 2:
            x_change = 0
            y_change = 1

        # right
        elif direc % 4 == 3:
            x_change = 1
            y_change = 0

        # up
        elif direc% 4 == 0:
            x_change = 0
            y_change = -1

        curr_x += x_change
        curr_y += y_change
    return spiral


# finds index of target int for adjacent sum
def find_index (spiral, n):
    for y in range(len(spiral)):
        for x in range(len(spiral)):
            if spiral[y][x] == n:
                return [y, x]


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the  numbers adjacent to n in the spiral if n is outside the range
# return 0
def sum_adjacent_numbers (spiral, n):

    # subtracts target int from sum
    sum = -n
    index = find_index(spiral, n)
    y, x = index[0], index[1]

    # gets adjacent sum
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= y + i < len(spiral) and 0 <= x + j < len(spiral):
                sum += spiral[y + i][x + j]
    return sum


# read the input file
# create the spiral
# add the adjacent numbers
# print the result
def main():
    input_data = sys.stdin.read()
    input_data = list(map(int, input_data.split('\n')[:-1]))
    spiral = create_spiral(input_data[0])
    for x in range(1, len(input_data)):
        print(sum_adjacent_numbers(spiral, input_data[x]))


if __name__ == "__main__":
    main()