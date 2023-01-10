import time

class Link():
    ''' This class represents a link between data items only'''

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


class LinkedList():
    ''' This class implements the operations of a simple linked list'''

    def __init__(self):
        self.first = None

    def insertFirst(self, data):
        '''inset data at begining of a linked list'''
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink

    def insertLast(self, data):
        ''' Inset the data at the end of a linked list '''
        newLink = Link(data)
        current = self.first

        if (current == None):
            self.first = newLink
            return
        # find the last and insert it there.
        while (current.next != None):
            current = current.next

        current.next = newLink

    def findLink(self, data):
        ''' find to which data is the link of a given data inside this linked list'''
        current = self.first
        if (current == None):
            return None

        # search and find the position of the given data, the get the link if.
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    def deleteLink(self, data):
        ''' Removes the data from the list if exist and fix the link problems.'''

        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current

            current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    def __str__(self):
        return str(self.first)


class Stack (object):

    def __init__ (self):
        self.l_list = LinkedList()
        self.last_insert = None
        self.length = 0
    # add an item to the top of the stack
    def push (self, item):
        self.length += 1
        self.last_insert = item
        self.l_list.insertLast(item)

    # remove an item from the top of the stack
    def pop(self):
        if not self.length == 0:
            self.l_list.deleteLink(self.last_insert)
            self.length -= 1

    # check if a stack is empty
    def isEmpty (self):
        return self.length == 0

    # return the number of elements in the stack
    def size(self):
        return self.length

    # a string representation of this stack.
    def __str__(self):
        return str(self.l_list)

my_stack = Stack()

# Push 10
start = time.time()
my_stack.push(10)
finish = time.time()
print(my_stack)
print("Time: " + str(finish - start))

# Push 18
start = time.time()
my_stack.push(18)
finish = time.time()
print(my_stack)
print("Time: " + str(finish - start))


# Push 1024
start = time.time()
my_stack.push(1024)
finish = time.time()
print(my_stack)
print("Time: " + str(finish - start))


# pop()
start = time.time()
print("pop()  ", my_stack.pop())
finish = time.time()
print("Time: " + str(finish - start))


# # peek()
# print("peak()  ", my_stack.peek())


# isEmpty()
start = time.time()
print("isEmpty()   ", my_stack.isEmpty())
finish = time.time()
print("Time: " + str(finish - start))