#  File: ExpressionTree.py
#  Description:
#  Student Name: Sneha Kamal
#  Student UT EID: sk52223
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number:52520
#  Date Created: 10/17/2022
#  Date Last Modified: 10/17/2022
import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack(object):
    def __init__(self):
        self.stack = []

    # add item to top of stack
    def push(self, data):
        self.stack.append(data)

    # remove item from top of stack
    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    # checks if stack is empty
    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild
    def __str__(self):
        return '(' + str(self.data) + ')'

class Tree(object):
    def __init__(self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        expr = expr.split(' ')
        tree_stack = Stack()
        self.root = Node()
        curr = self.root
        for c in expr:
            if c == '(':
                tree_node = Node()
                curr.lChild = tree_node
                tree_stack.push(curr)
                curr = curr.lChild
            elif c in operators:
                curr.data = c
                tree_stack.push(curr)
                tree_node = Node()
                curr.rChild = tree_node
                curr = curr.rChild
            elif c == ')':
                if not tree_stack.is_empty():
                    curr = tree_stack.pop()
            elif c != ' ':
                curr.data = c
                curr = tree_stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        if aNode.lChild == None and aNode.rChild == None:
            return str(aNode.data)
        else:
            return eval(f'{self.evaluate(aNode.lChild)} {aNode.data} {self.evaluate(aNode.rChild)}')
    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        if aNode.lChild == None and aNode.rChild == None:
            return str(aNode.data)
        else:
            return f'{aNode.data} {self.pre_order(aNode.lChild)} {self.pre_order(aNode.rChild)}'
    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        if aNode.lChild == None and aNode.rChild == None:
            return str(aNode.data)
        else:
            return f'{self.post_order(aNode.lChild)} {self.post_order(aNode.rChild)} {aNode.data}'

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    # create expression tree
    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root) / 1))
    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())
    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()  # the tree's expression
