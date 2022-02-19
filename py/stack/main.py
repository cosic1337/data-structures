from stack import Stack

if __name__ == '__main__':
    s = Stack()
    for i in range(16):
        s.push(i)

    for i in range(16):
        print(s.pop())

    print(len(s))