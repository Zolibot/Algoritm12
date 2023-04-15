# 85771865
from enum import IntEnum


class DequeError(Exception):
    def __init__(self):
        super().__init__("error")


class FullDequeError(DequeError):
    pass


class EmptyDequeError(DequeError):
    pass


class Step(IntEnum):
    NEXT: int = 1
    LAST: int = -1


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

    def get_index(self, index, step: Step):
        return (index + step) % self.max_size

    def push_front(self, value):
        if not self.is_full():
            self.deque[self.tail] = value
            self.tail = self.get_index(self.tail, Step.NEXT)
            self.size += 1
        else:
            raise FullDequeError()

    def push_back(self, value):
        if not self.is_full():
            self.head = self.get_index(self.head, Step.LAST)
            self.deque[self.head] = value
            self.size += 1
        else:
            raise FullDequeError()

    def pop_back(self, agrs=None):
        if self.is_empty():
            raise EmptyDequeError()
        value = self.deque[self.head]
        self.head = self.get_index(self.head, Step.NEXT)
        self.size -= 1
        return value

    def pop_front(self, agrs=None):
        if self.is_empty():
            raise EmptyDequeError()
        self.tail = self.get_index(self.tail, Step.LAST)
        value = self.deque[self.tail]
        self.size -= 1
        return value


def load_data():
    file = open("./input.txt", "rt")
    _ = int(file.readline())
    max_len_queue = int(file.readline())
    commands = [x for x in file.read().split("\n")]
    deque = Deque(max_len_queue)
    for cmd in commands:
        deque_processing(cmd, deque)


def deque_processing(cmd: str, deque: Deque):
    cmd,  *args = cmd.split() * 2
    try:
        msg = getattr(deque, cmd)(args[0])
        if msg is not None:
            print(msg)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    load_data()
