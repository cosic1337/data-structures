class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self._size
    
    def push(self, val):
        if self.is_empty():
            self.push_front(val)
        else:
            n = ListNode(val)
            self.tail.next = n
            self.tail = n
            self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        if self.size() == 1:
            return self.pop_front()
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
        tmp_val = curr.val
        prev.next = None
        self.tail = prev
        self._size -= 1
        return tmp_val

    def pop_front(self):
        if self.is_empty():
            return None
        if self.size() == 1:
            tmp_val = self.head.val
            self.head = self.tail = None
            self._size -= 1
            return tmp_val
        tmp_val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return tmp_val
        
    def push_front(self, val):
        n = ListNode(val)
        if self.is_empty():
            self.head = self.tail = n
            self._size += 1
        else:
            n.next = self.head
            self.head = n
            self._size += 1

    def value_at(self, idx):
        if idx < 0 or idx >= self.size():
            raise IndexError('Index out of range')
        if idx == 0:
            return self.front().val
        if idx == self.size() - 1:
            return self.back().val
        curr, i = self.head.next, 1
        while curr:
            if i == idx:
                return curr.val
            curr = curr.next
            i += 1        
        return None

    def front(self):
        return self.head

    def back(self):
        return self.tail

    def insert(self, idx, val):
        if idx < 0 or idx > self.size():
            raise IndexError('Index out of range')
        if idx == 0:
            self.push_front(val)
        elif idx == self.size():
            self.push(val)
        else:
            curr, i = self.head.next, 1
            prev = self.head
            while curr:
                if i == idx:
                    n = ListNode(val)
                    n.next = curr
                    prev.next = n
                    self._size += 1
                    break
                prev = curr
                curr = curr.next
                i += 1

    def delete(self, idx):
        if idx < 0 or idx >= self.size():
            raise IndexError('Index out of range')
        if idx == 0:
            return self.pop_front()
        if idx == self.size() - 1:
            return self.pop()
        curr, prev = self.head.next, self.head
        i = 1
        while curr:
            if i == idx:
                tmp_val = curr.val
                prev.next = curr.next
                self._size -= 1
                return tmp_val
            prev = curr
            curr = curr.next
            i += 1
    def reverse(self):
        if self.is_empty():
            raise Exception('Can\'t reverse empty list')
        if self.size() == 1:
            return self.head
        curr, prev = self.head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.tail = self.head
        self.head = prev
        return self.head
    