import time


class Stack (object):

    def __init__ (self):
        self.stack = []

  # add an item to the top of the stack
    def push (self, item):
        self.stack.append(item)

  # remove an item from the top of the stack
    def pop(self):
        if(not self.isEmpty()):
            return self.stack.pop()
        else:
            return None

  # check what item is on top of the stack without removing it
    def peek(self):
        return self.stack[len(self.stack) - 1]

  # check if a stack is empty
    def isEmpty (self):
        return (len(self.stack) == 0)

  # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

  # a string representation of this stack.
    def __str__(self):
        return str(self.stack)


# # a different implementation of the Stack class
# class Stack (object):
#   def __init__ (self):
#     self.stack = []

#   def push (self, item):
#     self.stack.insert(0, item )

#   def pop(self):
#     return self.stack.pop(0)

#   def peek (self):
#     return self.stack[0]

#   def isEmpty (self):
#     return (len(self.stack) == 0)

#   def size (self):
#     return (len(self.stack))

class Queue (object):
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, item):
        if not self.size() == 0:
            if self.enqueue_stack.isEmpty():
                for i in range(self.dequeue_stack.size()):
                    self.enqueue_stack.push(self.dequeue_stack.pop())
        self.enqueue_stack.push(item)

    def dequeue(self):
        if not self.size() == 0:
            if self.dequeue_stack.isEmpty():
                for i in range(self.enqueue_stack.size()):
                    self.dequeue_stack.push(self.enqueue_stack.pop())
            return self.dequeue_stack.pop()
        else:
            return None

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return max(self.enqueue_stack.size(), self.dequeue_stack.size())

    # a string representation of this stack.
    def __str__(self):
        if self.enqueue_stack.isEmpty():
            for i in range(self.dequeue_stack.size()):
                self.enqueue_stack.push(self.dequeue_stack.pop())
        return str(self.enqueue_stack)


my_queue = Queue()

# enqueue 10
start = time.time()
my_queue.enqueue(10)
finish = time.time()
print(my_queue)
print("Time: " + str(finish - start))

# enqueue 18
start = time.time()
my_queue.enqueue(18)
finish = time.time()
print(my_queue)
print("Time: " + str(finish - start))

# enqueue 1024
start = time.time()
my_queue.enqueue(1024)
finish = time.time()
print(my_queue)
print("Time: " + str(finish - start))


# dequeue()
start = time.time()
print("Dequeue ", my_queue.dequeue())
finish = time.time()
print("Time: " + str(finish - start))
start = time.time()
print("Dequeue ", my_queue.dequeue())
finish = time.time()
print("Time: " + str(finish - start))
start = time.time()
print("Dequeue ", my_queue.dequeue())
finish = time.time()
print("Time: " + str(finish - start))
start = time.time()
print("Dequeue ", my_queue.dequeue())
finish = time.time()
print("Time: " + str(finish - start))

# Time observations: used the model tests given, first enqueue is the longest then rest take approx. same
# amount of time. similarly for dequeue, first takes longest, rest take approx. same amount of time.
# enqueuing is faster than dequeuing