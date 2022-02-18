class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
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
        curr = self.head
        i = 0
        while curr:
            if i == idx:
                return curr.val
            i += 1
            curr = curr.next

    def push_front(self, val):
        n = ListNode(val)
        tmp = self.head
        self.head = n
        n.next = tmp
        self._size += 1

    def pop_front(self):
        if self.empty():
            return None
        tmp = self.head
        self.head = self.head.next
        tmp2 = tmp.val
        tmp = None
        self._size -= 1
        return tmp2

    def push_back(self, val):
        if self.empty():
            self.push_front(val)
        else:
            n = ListNode(val)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = n
            self._size += 1

    def pop_back(self):
        if self.empty():
            return None
        if self.size() == 1:
            return self.pop_front()
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
        tmp = curr.val
        prev.next = None
        curr = None
        self._size -= 1
        return tmp

    def front(self):
        if not self.empty():
            return None
        return self.head.val

    def back(self):
        if self.empty():
            raise Exception('Empty list')
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.val

    def insert(self, idx, val):
        if idx > self.size():
            raise IndexError('Index out of range')
        if idx == 0:
            self.push_front(val)
        elif idx == self.size():
            self.push_back(val)
        else:
            i = 1
            curr = self.head.next
            prev = self.head
            while curr:
                if idx == i:
                    n = ListNode(val)
                    prev.next = n
                    n.next = curr
                    self._size += 1
                    return n.val
                i += 1
                prev = curr
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
        curr = self.head.next
        prev = self.head
        i = 1
        while curr:
            if i == idx:
                next = curr.next
                tmp = curr.val
                prev.next = next
                curr = None
                self._size -= 1
                return tmp
            i += 1
            prev = curr
            curr = curr.next

    def reverse(self):
        if self.empty():
            raise Exception('Can\'t reverse empty list')
        if self.size() == 1:
            return
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

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

def print_nodes(head):
    if not head:
        return
    print(f'{head.val}=>', end='')
    print_nodes(head.next)
        

def singly():
    pass

def doubly():
    dl = DoublyLinkedList()
    for i in range(10):
        dl.push_back(i)
    print_nodes(dl.head)
    dl.reverse()
    print()
    print_nodes(dl.head)

def main():
    singly()
    doubly()

if __name__ == '__main__':
    main()
