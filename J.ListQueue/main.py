

class Node:
    def __init__(self, value, next_item=None, prev_item=None):
        self.value = value
        self.next_item = next_item
        self.prev_item = prev_item


class LinkListQueue:
    def __init__(self):
        self.head = None
        self.start = None
        self.size = 0
        self.COMMAND = {
            'put': self.put,
            'get': self.get,
            'size': self.get_size,
        }

    def put(self, value):
        if self.size == 0:
            self.size += 1
            self.head = Node(value, None)
            self.start = self.head
        else:
            self.size += 1
            tmp = Node(value, None, self.head)
            self.head.next_item = tmp
            self.head = tmp

    def get(self):
        if self.size == 0:
            return print("error")
        self.size -= 1
        value = self.start.value
        self.start = self.start.next_item
        return print(value)

    def get_size(self):
        return print(self.size)


def load_data():
    file = open('./input.txt', 'rt')
    commands_len = int(file.readline().strip())
    commands = [x for x in file.read().split('\n')]
    queue = LinkListQueue()
    for command in commands:
        stack_interface(command, queue)


def stack_interface(data: str, queue: LinkListQueue):
    command = data.split()
    length = len(command)
    if length > 1:
        queue.COMMAND[data.split()[0]](int(data.split()[1]))
    elif length == 1:
        queue.COMMAND[data.split()[0]]()


if __name__ == '__main__':
    load_data()
    # import timeit
    #
    # print(timeit.timeit('load_data()', number=1000, setup='from __main__ import load_data'))
