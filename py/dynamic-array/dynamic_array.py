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
            self.allocate_new_arr()
        self.arr[self._size] = val
        self._size += 1
    
    def pop(self, val):
        if self._size == 0:
            return None
        tmp = self.arr[self._size - 1]
        self.arr[self._size - 1] = None
        self._size -= 1
        return tmp

    def remove(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError('Index out of range')
        for i in range(idx, self._size - 1):
            self.arr[j] = self.arr[j+1]
        self._size -= 1

    def allocate_new_arr(self):
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity
        for i in range(self._size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def size(self):
        return self._size

    def __len__(self):
        return self._size
