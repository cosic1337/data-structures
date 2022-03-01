class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def enqueue(self, val):
        n = ListNode(val)
        if self.empty():
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def dequeue(self):
        if self.empty():
            raise Exception('Dequeuing empty queue')
        self.head = self.head.next

    