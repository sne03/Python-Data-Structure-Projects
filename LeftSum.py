#  File: LeftSum.py
#  Description: Get the left sum of the BST
#  Student Name:
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number: 86610
import sys
class Queue(object):
    def __init__(self):
        self.queue = []
    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))
    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)
    # return the size of the queue
    def size(self):
        return (len(self.queue))
class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None
class Tree (object):
  def __init__ (self):
    self.root = None
  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)
    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild
      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  def recursive_get_level(self, level, curr_level, curr_node, ans_list):
      if curr_level == level:
          ans_list.append(curr_node)
      else:
          if curr_node.lchild is not None:
              self.recursive_get_level(level, curr_level + 1, curr_node.lchild, ans_list)
          if curr_node.rchild is not None:
              self.recursive_get_level(level, curr_level + 1, curr_node.rchild, ans_list)

  # Returns a list of nodes at a given level from left to right
  def get_level(self, level):
      ans_list = []
      if self.root is None:
          return ans_list
      self.recursive_get_level(level, 0, self.root, ans_list)
      return ans_list

  def left_side_view(self):
      left_list = []
      #height = self.root.get_height()
      i = 0
      while(len(self.get_level(i))):
          left_list.append(self.get_level(i)[0].data)
          i+=1
      return left_list

  # Returns an integer for the left sum of the BST
  def get_left_sum(self):
    sum = 0
    left_list = self.left_side_view()
    for i in range(len(left_list)):
        sum += left_list[i]
    return sum

# ***There is no reason to change anything below this line***
def main():
    # Create tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list (map (int, line))    # converts elements into ints
    tree = Tree()
    for i in tree_input:
      tree.insert(i)
    print(tree.get_left_sum())
if __name__ == "__main__":
  main()