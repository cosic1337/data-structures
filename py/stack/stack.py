class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, val):
        n = ListNode(val)
        n.next = self.head
        self.head = n
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        tmp_val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return tmp_val

    def __len__(self):
        return self.size()