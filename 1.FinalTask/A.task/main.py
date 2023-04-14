# 85771865
class DecQueue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return "error"

    def push_back(self, x):
        if self.size != self.max_n:
            self.head = (self.head - 1) % self.max_n
            self.queue[self.head] = x
            self.size += 1
        else:
            return "error"

    def pop_back(self):
        if self.is_empty():
            return "error"
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            return "error"
        self.tail = (self.tail - 1) % self.max_n
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        self.size -= 1
        return x


def load_data():
    file = open("./input.txt", "rt")
    _ = int(file.readline())
    max_len_queue = int(file.readline())
    commands = [x for x in file.read().split("\n")]
    queue = DecQueue(max_len_queue)
    for cmd in commands:
        queue_interface(cmd, queue)


def queue_interface(data: str, queue: DecQueue):
    command = {
        "push_front": queue.push_front,
        "push_back": queue.push_back,
        "pop_front": queue.pop_front,
        "pop_back": queue.pop_back,
    }
    cmd = data.split()
    length = len(cmd)
    msg = None
    if length > 1:
        msg = command[cmd[0]](int(cmd[1]))
    elif length == 1:
        msg = command[cmd[0]]()

    if msg is not None:
        print(msg)


if __name__ == "__main__":
    load_data()
