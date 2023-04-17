# 85939044
from typing import Optional


class DequeException(Exception):
    """ Base class deque exception. """
    def __init__(self, *args):
        super().__init__(*args)
        print(*args)


class FullDequeError(DequeException):
    """ Deque size exceeded. """

    pass


class EmptyDequeError(DequeException):
    """ Emptying the deque. """
    pass


class Deque:
    def __init__(self, size):
        self.deque = [None] * size
        self.max_size = size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def get_index(self, index, add: bool):
        index = index + 1 if add else index - 1
        return index % self.max_size

    def push_front(self, value):
        if self.is_full():
            raise FullDequeError('error')
        self.deque[self.tail] = value
        self.tail = self.get_index(self.tail, False)
        self.size += 1

    def push_back(self, value):
        if self.is_full():
            raise FullDequeError('error')
        self.head = self.get_index(self.head, True)
        self.deque[self.head] = value
        self.size += 1

    def pop_back(self, args=None):
        if self.is_empty():
            raise EmptyDequeError('error')
        value = self.deque[self.head]
        self.head = self.get_index(self.head, False)
        self.size -= 1
        return value

    def pop_front(self, args=None):
        if self.is_empty():
            raise EmptyDequeError('error')
        self.tail = self.get_index(self.tail, True)
        value = self.deque[self.tail]
        self.size -= 1
        return value


def load_data():
    file = open('./input.txt', 'rt')
    order_count = int(file.readline())
    max_len_deque = int(file.readline())
    orders = file.read().split('\n')
    return orders, order_count, max_len_deque


def deque_handle(data: str, deq: Deque) -> Optional[str]:
    data = data.split()
    info = None
    try:
        info = getattr(deq, data[0])(*data[1:])
    except (FullDequeError, EmptyDequeError):
        pass

    return info


if __name__ == '__main__':
    commands, count, size_deque = load_data()
    deque = Deque(size_deque)
    for index in range(count):
        message = deque_handle(commands[index], deque)
        if message is not None:
            print(message)
