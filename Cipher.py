# File: Cipher.py

# Description: Encryption and Decryption

# Student Name: Sneha Kamal

# Student UT EID: sk52223

# Course Name: CS 313E

# Unique Number: 52520

# Date Created: 09/12/2022

# Date Last Modified: 09/14/2022

import math
import sys


# Input: string is a string of 100 or less of upper case, lower case, and digits
# Output: function returns an encrypted string
def encrypt(string_p):
    padded_msg = string_p
    encrypted_string = ''

    # gets message length (L)
    length = len(string_p)

    # sets init smallest square value (M)
    small_sqr = length

    # sets init K
    k = math.sqrt(small_sqr)

    # finds smallest square number
    while k * k != small_sqr:
        small_sqr += 1
        k = math.sqrt(small_sqr)
    table_size = int(k)

    # creates table
    if small_sqr % k != 0:
        table_size += 1
    num_ast = table_size**2 - length
    table = [[0 for i in range(table_size)] for j in range(table_size)]

    # pads message
    for x in range(num_ast):
        padded_msg += "*"

    # fills table
    for y in range(len(table)):
        for x in range(len(table)):
            table[y][x] = padded_msg[x + (table_size * y)]

    # rotates table, gets encrypted message
    for x in range(len(table)):
        for y in range(len(table) - 1, -1, -1):
            encrypted_string += table[y][x]

    return encrypted_string.replace('*', '')


# Input: string is a string of 100 or less of upper case, lower case, and digits
# Output: function returns a decrypted string
def decrypt(string_q):
    decrypted_string = ''

    # gets message length (L)
    length = len(string_q)
    # sets init smallest square value (M)
    small_sqr = length

    # sets init K
    k = math.sqrt(small_sqr)

    # finds smallest square number
    while k * k != small_sqr:
        small_sqr += 1
        k = math.sqrt(small_sqr)

    # creates table
    table_size = int(math.sqrt(small_sqr))
    if small_sqr % k != 0:
        table_size += 1
    num_ast = table_size**2 - length
    table = [[0 for i in range(table_size)] for j in range(table_size)]

    # starting point for asterisks
    spec_num = table_size**2 - num_ast
    curr_x = 0
    curr_y = table_size - 1

    # puts asterisks in table
    for i in range(num_ast):
        table[curr_y][curr_x] = '*'
        curr_y -= 1
        if curr_y < 0:
            curr_y = table_size - 1
            curr_x += 1

    # fills table with message
    curr_string_ind = 0
    for y in range(len(table)):
        for x in range(len(table)):
            if table[y][x] == 0:
                table[y][x] = string_q[curr_string_ind]
                curr_string_ind += 1

    # rotates table, gets decrypted message
    for x in range(len(table) - 1, -1, -1):
        for y in range(len(table)):
            decrypted_string += table[y][x]

    return decrypted_string.replace('*', '')


# Read two strings P and Q from standard input
# Encrypt string P
# Decrypt string Q
# print encrypted string of P and decrypted string of Q to standard out
def main():
    read = sys.stdin.read()
    new_ln_loc = read.find('\n', 0, len(read))
    p = read[0:new_ln_loc]
    q = read[new_ln_loc + 1:]
    print(encrypt(p.replace('\n', '')))
    print(decrypt(q.replace('\n', '')))


if __name__ == "__main__":
    main()
