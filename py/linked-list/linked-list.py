from singly import SinglyLinkedList as singly
from doubly import DoublyLinkedList as doubly
from helpers import print_nodes, generate_nodes, del_nodes

def test_list(list=None, size=0, del_size=0):
    generate_nodes(size, list)
    assert list.size() == size
    head, tail = list.front(), list.back()
    list.reverse()
    assert head == list.back() and tail == list.front()
    del_nodes(del_size, list)
    assert list.size() == size - del_size

def main():
    sl = singly()
    dl = doubly()
    test_list(sl, 30, 10)
    test_list(dl, 30, 10)

if __name__ == '__main__':
    main()
