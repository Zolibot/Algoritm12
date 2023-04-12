# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def print_node(node):
    while node:
        print(node.value, end="->")
        node = node.next_item


def solution(node, idx):
    def get_node(n, i):
        while i:
            n = n.next_item
            i -= 1
        return n
    if idx == 0:
        node = node.next_item
    else:
        prev_n = get_node(node, idx - 1)
        next_n = get_node(node, idx + 1)
        prev_n.next_item = next_n
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    print_node(node0)
    print()
    new_head = solution(node0, 1)
    print_node(new_head)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


# if __name__ == '__main__':
#     test()
