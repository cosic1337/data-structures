class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def empty(self):
        return self.head == None
    
    def size(self):
        return self._size

    def push(self, val):
        n = ListNode(val)
        n.next = self.head
        self.head = n
        self._size += 1

    def pop(self, val):
        if self.empty():
            raise Exception('Popping empty stack')
        tmp = self.head
        self.head = self.head.next
        self._size -= 1
        return tmp