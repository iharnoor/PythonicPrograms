"""Simple List operations for a queue"""

class MyQueue(object):
    def __init__(self):
        self.myList = []

    def peek(self):
        return self.myList[0]

    def dequeue(self):
        return self.myList.pop(0)

    def enqueue(self, value):
        self.myList.append(value)


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
