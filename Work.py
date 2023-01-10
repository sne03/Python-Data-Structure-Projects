# File: Work.py

# Description: Chris has to complete a programming assignment overnight. He has to write n lines of code before morning.
# He is dead tired and he tries drinking some black coffee to keep him awake. But each time he drinks a cup
# of coffee he stays awake for a short amount of time but his productivity goes down by a constant factor k
# This is how he plans to write the program. He will write the first v lines of code, then drink his first cup
# of coffee.
# •Since his productivity has gone down by a factor of k he will write v // k lines of code.
# •He will have another cup of coffee and then write v // k**2 lines of code.
# •He will have another cup of coffee and write v // k**3 lines of code and so on.
# •He will collapse and fall asleep when v // k ** p becomes 0.
# Now Chris does want to complete his assignment and maximize on his sleep. So he wants to figure out
# the minimum allowable value of v for a given productivity factor that will allow him to write at least n lines
# of code before he falls asleep.

# Student Name: Sneha Kamal

# Student UT EID: sk52223

# Course Name: CS 313E

# Unique Number: 52520

# Date Created: 10/03/2022

# Date Last Modified:

# Input: You will read your input from standard input as given in the following format file work.in:
# 1 2
# 2 3 0 0 2
# 3 59 9
# The first line is T the number of test cases. This will be followed by T lines of input. Each line of input
# will have two numbers nand k. nis the number of lines of code to write and kis the productivity factor,
# where 1 ≤n≤106and 2 ≤k≤10.

# Output: For each test case write your result to standard out as shown in file work.out. In your output there will be
# v lines of code the Chris has to write, as well as the time it took for each function. For the above two test
# cases, the output will be:
# 1
# 1 B i n a r y S e a r c h : 1 5 2
# 2 Time : 9 . 5 1 2 9 0 1 3 0 6 1 5 2 3 4 4 e −05
# 3
# 4 L i n e a r S e a r c h : 1 5 2
# 5 Time : 0 . 0 0 0 5 9 1 0 3 9 6 5 7 5 9 2 7 7 3 4
# 6
# 7
# 8 B i n a r y S e a r c h : 54
# 9 Time : 4 . 6 9 6 8 4 6 0 0 8 3 0 0 7 8 1 e −05
# 10
# 11 L i n e a r S e a r c h : 54
# 12 Time : 9 . 0 1 2 2 2 2 2 9 0 0 3 9 0 6 2 e −05
# 13
# Do not worry if your times do not match ours exactly. They are given just for comparison purposes. For
# this assignment, main has been written completely for you, and nothing needs to be changed in it.
# You will be solving this problem in 2 ways. First, you will write a function that uses a linear search to
# solve the problem. Then you will write a function that uses a modified binary search algorithm to solve it
# again. Both functions will return the same answer, but the binary search method will usually be faster.
# It is recommended that you write a helper function, which given a value v representing the number of
# lines Chris writes before his first cup of coffee and a value k, the productivity factor, will calculate the
# number of lines Chris will write before falling asleep. This can be called in both the linear and binary
# functions to make the computations easier.

import time
import sys


# sums equation, checks if v value allows for at least n lines of code to be written
def sum_equation(v, k):
    solution = 0
    num_lines = v
    exponent = 0
    while num_lines > 0:
        num_lines = v // k**exponent
        solution += num_lines
        exponent += 1
    return solution


# returns minimum v value in order for at least n lines of code to be written
def linear_search(n, k):
    for i in range(0, n + 1):
        if sum_equation(i, k) >= n:
            return i


def binary_search(n, k):
    search_min = 0
    search_max = n
    current = n // 2
    answer = sum_equation(current, k)
    while current != search_min:
        if answer == n:
            return current
        elif answer < n:
            search_min = current
            current = (search_min + search_max) // 2
        # answer > n
        else:
            search_max = current
            current = (search_min + search_max) // 2
        answer = sum_equation(current, k)

    # if n not found
    return current + 1


def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int(line)
    for i in range(num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp = line.split()
        n = int(inp[0])
        k = int(inp[1])
        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))
        print()
        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))
        print()
        print()


if __name__ == "__main__":
    main()








