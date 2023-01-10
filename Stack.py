import time


class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if (not self.isEmpty()):
            return self.queue.pop(0)
        else:
            return None

    def isEmpty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)

    # a string representation of this stack.
    def __str__(self):
        return str(self.queue)

class Stack (object):

    def __init__ (self):
        self.queue_1 = Queue()
        self.queue_2 = Queue()

    # add an item to the top of the stack
    def push (self, item):
        self.queue_1.enqueue(item)

    # remove an item from the top of the stack
    def pop(self):
        while self.queue_1.size() > 1:
            self.queue_2.enqueue(self.queue_1.dequeue())
        temp = self.queue_1.dequeue()
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1
        return temp

    # check if a stack is empty
    def isEmpty (self):
        return self.queue_1.size() == 0

    # return the number of elements in the stack
    def size(self):
        return self.queue_1.size()

    # a string representation of this stack.
    def __str__(self):
        return str(self.queue_1)


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

start = time.time()
print("pop()  ", my_stack.pop())
finish = time.time()
print("Time: " + str(finish - start))
start = time.time()
print("pop()  ", my_stack.pop())
finish = time.time()
print("Time: " + str(finish - start))
start = time.time()
print("pop()  ", my_stack.pop())
finish = time.time()
print("Time: " + str(finish - start))
start = time.time()
print("isEmpty()   ", my_stack.isEmpty())
finish = time.time()
print("Time: " + str(finish - start))

# Time observation: pushing gets faster after adding each item. popping is slowest for the first time, rest
# take approx. same amount of time. overall, pushing is faster.