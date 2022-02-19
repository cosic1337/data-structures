class DynamicArray:
    def __init__(self, capacity=2):
        self._size = 0
        self.capacity = max(2, capacity)
        self.arr = [None] * self.capacity

    def get(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError('Index out of range')
        return self.arr[idx]

    def push(self, val):
        if self._size == self.capacity:
            self.resize()
        self.arr[self._size] = val
        self._size += 1
    
    def pop(self, val):
        if self._size == 0:
            return None
        tmp = self.arr[self._size - 1]
        self.arr[self._size - 1] = None
        self._size -= 1
        return tmp

    def delete(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError('Index out of range')
        for i in range(idx, self._size - 1):
            self.arr[j] = self.arr[j+1]
        self._size -= 1

    def remove(self, item):
        for i in range(self.size()):
            if self.arr[i] == item:
                self.delete(i)

    def find(self, item):
        for i in range(self.size()):
            if self.arr[i] == item:
                return self.arr[i]
        return -1

    def resize(self):
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity
        for i in range(self._size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def size(self):
        return self._size

    def capacity(self):
        return self.capacity

    def isempty(self):
        return self._size == 0

    def __len__(self):
        return self._size
