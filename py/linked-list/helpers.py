def print_nodes(head):
    if not head:
        return
    print(f'{head.val}=>', end='')
    print_nodes(head.next)

def generate_nodes(amount=10, list=None):
    if not list:
        return
    for i in range(amount):
        list.push(i)

def del_nodes(amount=0, list=None):
    if not list:
        return
    for _ in range(amount):
        list.pop()