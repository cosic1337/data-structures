class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def empty(self):
        return self.head == None

    def value_at(self, idx):
        if self.empty():
            return None
        if idx >= self.size():
            raise IndexError('Index out of range')
        if idx > self.size() // 2:
            curr = self.tail
            i = self.size() - 1
            while curr:
                if i == idx:
                    return curr.val
                i -= 1
                curr = curr.prev
        else:
            curr = self.head
            i = 0
            while curr:
                if i == idx:
                    return curr.val
                i += 1
                curr = curr.next

    def push_front(self, val):
        n = ListNode(val)
        if self.empty():
            self.head = self.tail = n
            self._size += 1
        else:
            tmp = self.head
            self.head = n
            n.next = tmp
            tmp.prev = n
            self_size += 1

    def pop_front(self):
        if self.empty():
            return None
        tmp, tmp_val = self.head, self.head.val
        self.head = self.head.next
        self.head.prev = tmp = None
        self._size -= 1
        return tmp_val

    def push_back(self, val):
        if self.empty():
            self.push_front(val)
        else:
            n = ListNode(val)
            tmp = self.tail
            self.tail = n
            tmp.next = n
            n.prev = tmp
            self._size += 1

    def pop_back(self):
        if self.empty():
            return None
        if self.size() == 1:
            tmp = self.head.val
            self.head = self.tail = None
            self._size -= 1
            return tmp
        tmp, tmp_val = self.tail, self.tail.val
        self.tail = self.tail.prev
        self.tail.next = tmp = None
        self._size -= 1
        return tmp_val
    
    def front(self):
        if self.empty():
            return None
        return self.head.val

    def back(self):
        if self.empty():
            return None
        return self.tail.val
    
    def insert(self, idx, val):
        if idx > self.size():
            raise IndexError('Index out of range')
        if idx == 0:
            self.push_front(val)
        elif idx == self.size():
            self.push_back(val)
        else:
            if(idx > self.size() // 2):
                i = self.size() - 2
                curr = self.tail.prev
                while curr:
                    if idx == i:
                        n = ListNode(val)
                        curr.next.prev = n
                        n.next = curr.next.prev
                        curr.next = n
                        n.prev = curr
                        self._size += 1
                        return n.val
                    i -= 1
                    curr = curr.prev
            else:
                curr = self.head.next
                i = 1
                while curr:
                    if i == idx:
                        n = ListNode(val)
                        curr.next.prev = n
                        n.next = curr.next.prev
                        curr.next = n
                        n.prev = curr
                        self._size += 1
                        return n.val
                    i += 1
                    curr = curr.next

    def erase(self, idx):
        if self.empty():
            return None
        if idx >= self.size():
            raise IndexError('Index out of range')
        if idx == 0:
            return self.pop_front()
        if idx == self.size() - 1:
            return self.pop_back()
        if idx > self.size() // 2:
            curr = self.tail.prev
            i = self.size() - 2
            while curr:
                if i == idx:
                    tmp_val = curr.val
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    curr = curr.val = None
                    self._size -= 1
                    return tmp_val
                i -= 1
                curr = curr.prev
        else:
            curr = self.head.next
            i = 1
            while curr:
                if i == idx:
                    tmp_val = curr.val
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    curr = curr.val = Nonje
                    self._size -= 1
                    return tmp_val
                i += 1
                curr = curr.next

    def reverse(self):
        if self.empty():
            raise Exception('Can\'t reverse empty list')
        if self.size() == 1:
            return
        curr = self.head
        prev = self.head.prev
        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        tmp = self.head
        self.head = self.tail
        self.tail = tmp