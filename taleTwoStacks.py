"""
Program Name= Queues: A Tale of Two Stacks;
Purpose: To build a queue with the help of two stacks.
"""


class MyQueue(object):
    def __init__(self):
        self.stackNewestOnTop = []
        self.stackOldestOnTop = []

    def peek(self):
        self.shiftStacks()
        return self.stackOldestOnTop[-1]

    def dequeue(self):
        self.shiftStacks()
        return self.stackOldestOnTop.pop()

    def enqueue(self, value):
        self.stackNewestOnTop.append(value)

    def shiftStacks(self):
        if len(self.stackOldestOnTop) == 0:
            while len(self.stackNewestOnTop) != 0:
                self.stackOldestOnTop.append(self.stackNewestOnTop.pop())


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.enqueue(values[1])
    elif values[0] == 2:
        queue.dequeue()
    else:
        print(queue.peek())
