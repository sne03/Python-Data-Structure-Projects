# File: Anagrams.py
# Description: A program to group strings into anagram families
# Student Name: Sneha Kamal
# Student UT EID: sk52223
# Course Name: CS 313E
# Unique Number: 52520


# Output: True or False
def are_anagrams(str1, str2):
    for i in range(len(str1)):
        if str1.count(str1[i]) != str2.count(str1[i]):
            return False
    return True


# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    no_calc = []
    num_families = len(lst)
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if j not in no_calc:
                if are_anagrams(lst[i], lst[j]):
                    no_calc.append(j)
                    num_families -= 1
    return num_families


def main():
    # read the number of strings in the list
    num_strs = int(input())
    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]
    # compute the number of anagram families
    num_families = anagram_families(lst)
    # print the number of anagram families
    print(num_families)
if __name__ == "__main__":
    main()