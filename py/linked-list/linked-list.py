from singly import SinglyLinkedList as singly
from doubly import DoublyLinkedList as doubly
from helpers import print_nodes, generate_nodes, del_nodes

def singly_ll():
    sl = singly()
    generate_nodes(30, sl)
    assert sl.size() == 30
    head, tail = sl.front(), sl.back()
    sl.reverse()
    assert head == sl.back() and tail == sl.front()
    del_nodes(10, sl)
    assert sl.size() == 20

def doubly_ll():
    dl = doubly()
    generate_nodes(30, dl)
    assert dl.size() == 30
    head, tail = dl.front(), dl.back()
    dl.reverse()
    assert head == dl.back() and tail == dl.front()
    del_nodes(10, dl)
    assert dl.size() == 20

def main():
    singly_ll()
    doubly_ll()

if __name__ == '__main__':
    main()
