from dynamic_array import DynamicArray

if __name__ == '__main__':
    arr = DynamicArray()
    for i in range(50):
        arr.push(i)
    i = 0
    while arr.arr[i] is not None and i < arr.size():
        print(arr.arr[i])
        i += 1