#  File: TestBinaryTree.py
#  Description:
#  Student Name: Sneha
#  Student UT EID: Kamal
#  Partner Name: Vedanth
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52520
#  Date Created: 10/18/2022
#  Date Last Modified: 10/24/2022

import sys


class Node(object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def __str__(self):
        return str(self.data)

    def print_node(self, level=0):
        if self.lChild != None:
            self.lChild.print_node(level + 1)
        print(' ' * 3 * level + '->', self.data)
        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparison to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        curr = self.root
        while curr.rChild != None:
            curr = curr.rChild
        max_val = curr.data
        curr = self.root
        while curr.lChild != None:
            curr = curr.lChild
        min_val = curr.data
        return max_val - min_val

    def recursive_get_level(self, level, curr_level, curr_node, ans_list):
        if curr_level == level:
            ans_list.append(curr_node)
        else:
            if curr_node.lChild is not None:
                self.recursive_get_level(level, curr_level + 1, curr_node.lChild, ans_list)
            if curr_node.rChild is not None:
                self.recursive_get_level(level, curr_level + 1, curr_node.rChild, ans_list)

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        ans_list = []
        if self.root is None:
            return ans_list
        self.recursive_get_level(level, 0, self.root, ans_list)
        return ans_list

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        left_list = []
        height = self.root.get_height()
        for i in range(height):
            left_list.append(self.get_level(i)[0].data)
        return left_list

    def recursive_sum_leaf_nodes(self, curr, leaf_sum):
        if curr.lChild is None and curr.rChild is None:
            return curr.data
        else:
            if curr.lChild is not None and curr.rChild is not None:
                return leaf_sum + self.recursive_sum_leaf_nodes(curr.lChild, leaf_sum) + self.recursive_sum_leaf_nodes(
                    curr.rChild, leaf_sum)
            elif curr.lChild is not None:
                return leaf_sum + self.recursive_sum_leaf_nodes(curr.lChild, leaf_sum)
            elif curr.rChild is not None:
                return leaf_sum + self.recursive_sum_leaf_nodes(curr.rChild, leaf_sum)

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.

    def sum_leaf_nodes(self):
        x = self.recursive_sum_leaf_nodes(self.root, 0)
        return x


def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescope will import your classes and call the methods.
def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())
    print("Tree range is: ", t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")
    # Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())
    print("Tree range is: ", t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
    # Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())
    print("Tree range is: ", t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()