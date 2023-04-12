class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0
        self.COMMAND = {
            'push': self.push,
            'pop': self.pop,
            'peek': self.peek,
            'size': self.size_print,
        }

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return print('None')
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return print(x)

    def peek(self):
        if self.is_empty():
            return print('None')
        return print(self.queue[self.head])

    def size_print(self):
        return print(self.size)


def load_data():
    file = open('./input.txt', 'rt')
    commands_len = int(file.readline().strip())
    max_len_queue = int(file.readline().strip())
    commands = [x for x in file.read().split('\n')]
    queue = Queue(max_len_queue)
    for command in commands:
        stack_interface(command, queue)


def stack_interface(data: str, queue: Queue):
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
