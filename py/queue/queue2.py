# Implementation with fixed-size array
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.write = self.read = 0

    def full(self):
        return (self.write + 1) % self.size == self.read

    def empty(self):
        return self.write == self.read

    def enqueue(self, val):
        if self.full():
            raise Exception('Queue is full')
        self.queue[self.write] = val
        self.write = (self.write + 1) % self.size

    def dequeue(self):
        if self.empty():
            return None
        tmp = self.queue[self.read]
        self.queue[self.read] = None
        self.read = (self.read + 1) % self.size
        return tmp
    

    