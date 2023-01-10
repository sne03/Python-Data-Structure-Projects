# Student Name: Sneha Kamal

# Student UT EID: sk52223

# Course Name: CS 313E

# Unique Number: 52520

# Date Created: 10/10/2022

# Date Last Modified: 10/10/2022


import sys

class Link(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class CircularList(object):
    # Constructor
    def __init__ ( self ):
        self.first = None
        self.last = None

    # Insert an element (value) in the list
    def insert ( self, data ):
        new_val = Link(data)
        if self.first == None:
            self.first = new_val
            self.last = new_val
        self.last.next= new_val
        self.last = new_val
        self.last.next = self.first

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find ( self, data ):
        curr = self.first
        while curr != self.last:
            if curr.data - data == 0:
                return curr
            curr = curr.next
        if self.last.data == data:
            return self.last
        return None

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete ( self, data ):
        curr = self.first
        # if list empty
        if curr == None:
            return None

        # if only one element in list
        if curr == self.first and curr == self.last:
            self.first = None
            self.last = None

        # all other cases
        while curr != self.last:
            if curr.next.data == data and curr.next == self.last:
                self.last = curr
                break
            elif curr.next.data == data:
                break
            curr = curr.next
        else:
            if curr.next.data != data:
                return None
            else:
                self.first = curr.next.next
        link_deleted = curr.next
        curr.next = curr.next.next
        return link_deleted

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after (self, start, n):
        curr = self.find(start)
        link_deleted = None
        if curr != None:
            for i in range(n-1):
                curr = curr.next
            link_deleted = self.delete(curr.data)
            print(link_deleted)
        return link_deleted.data, curr.next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__ ( self ):
        circ_list = '['
        curr = self.first
        while curr != self.last:
            circ_list += str(curr) + ', '
            curr = curr.next
        if self.last != None:
            circ_list += str(self.last)
        circ_list += ']'
        return circ_list

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)
    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)
    # print("start count " + str(start_count))
    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)
    # your code
    circular_list = CircularList()
    for i in range(1, num_soldiers + 1):
        circular_list.insert(i)
    for i in range (num_soldiers):
        start_count = circular_list.delete_after(start_count, elim_num)[1].data


if __name__ == "__main__":
  main()
