class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

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
        
        tmp_val = self.tail.val
        self.tail.prev.next = None
        self.tail = self.tail.prev
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
        if idx > self.size() // 2:
            curr, i = self.tail.prev, self.size() - 2
            while curr:
                if i == idx:
                    return curr.val
                curr = curr.prev
                i -= 1
        else:
            curr, i = self.head.next, 1
            while curr:
                if i == idx:
                    return curr.val
                curr = curr.next
                i += 1

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
            if idx > self.size() // 2:
                curr, i = self.tail.prev, self.size() - 2
                while curr:
                    if i == idx:
                        n = ListNode(val)
                        n.next = curr
                        n.prev = curr.prev
                        curr.prev.next = n
                        curr.prev = n
                        self._size += 1
                        break
                    curr = curr.prev
                    i -= 1
            else:
                curr, i = self.head.next, 1
                while curr:
                    if i == idx:
                        n = ListNode(val)
                        n.next = curr
                        n.prev = curr.prev
                        curr.prev.next = n
                        curr.prev = n
                        self._size += 1
                        break
                    curr = curr.next
                    i += 1
    
    def delete(self, idx):
        if idx < 0 or idx >= self.size():
            raise IndexError('Index out of range')
        if idx == 0:
            return self.pop_front()
        if idx == self.size() - 1:
            return self.pop()
        if idx > self.size() // 2:
            curr, i = self.tail.prev, self.size() - 2
            while curr:
                if i == idx:
                    tmp_val = curr.val
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    self._size -= 1
                    return tmp_val
                curr = curr.prev
                i -= 1
        else:
            curr, i = self.head.next, 1
            while curr:
                if i == idx:
                    tmp_val = curr.val
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    self._size -= 1
                    return tmp_val
                curr = curr.next
                i += 1

    def reverse(self):
        if self.is_empty():
            raise Exception('Can\t reverse empty list')
        if self.size() == 1:
            return self.head
        curr = self.head
        prev = self.head.prev
        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        self.tail = self.head
        self.head = prev
        return self.head