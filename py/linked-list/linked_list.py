class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def size(self):
        return self._size
    
    def empty(self):
        return self.head == None
    
    def val_at(self, idx):
        curr, i = self.head, 0
        while curr:
            if i == idx:
                return curr.val
            i += 1
            curr = curr.next
        return None

    def push_front(self, val):
        n = ListNode(val)
        n.next = self.head
        self.head = n
        self._size += 1
    
    def pop_front(self):
        if self.empty():
            return None
        tmp = self.head
        self.head = self.head.next
        self._size -= 1
        return tmp

    def push_back(self, val):
        if self.empty():
            self.push_front(val)
        else:
            last = self.back()
            last.next = ListNode(val)
            self._size += 1

    def pop_back(self):
        if self.empty():
            return None
        if self.size() == 1:
            return self.pop_front()
        curr = self.head
        while curr.next.next:
            curr = curr.next
        tmp = curr.next
        curr.next = None
        self._size -= 1
        return tmp

    def front(self):
        return self.head

    def back(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr

    def insert(self, idx, val):
        if idx < 0 or idx > self.size():
            raise IndexError('Index out of range')
        if idx == 0:
            self.push_front(val)
        elif idx == self.size():
            self.push_back(val)
        else:
            curr, i = self.head.next, 1
            prev = self.head
            while curr:
                if i == idx:
                    n = ListNode(val)
                    prev.next = n
                    n.next = curr
                    self._size += 1
                prev = curr
                curr = curr.next
                i += 1

    def erase(self, idx):
        if idx < 0 or idx >= self.size():
            raise IndexError('Index out of range')
        if idx == 0:
            return self.pop_front()
        if idx == self.size() - 1:
            return self.pop_back()
        curr, i = self.head.next, 1
        prev = self.head
        while curr:
            if i == idx:
                prev.next = curr.next
                curr = curr.next = None
                self._size -= 1
            prev = curr
            curr = curr.next
            i += 1

    def value_n_from_end(self, n):
        if self.empty():
            return None
        fast = slow = self.head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return self.head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow.next

    def reverse(self):
        if self.empty():
            raise Exception('Empty list')
        if self.size() == 1:
            return self.head
        curr, prev = self.head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return self.head