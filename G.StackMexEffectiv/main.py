class Stack:
    def __init__(self):
        self.items = []
        self.max_value = []
        self.index = 0
        self.COMMAND = {
            "get_max": self.get_max,
            "push": self.push,
            "pop": self.pop,
        }

    def get_max(self):
        if self.index == 0:
            return print("None")
        print(self.max_value[-1])

    def push(self, item):
        if self.index == 0:
            self.max_value.append(item)

        self.index += 1
        self.items.append(item)

        max_val = self.max_value[-1]

        if max_val < item:
            self.max_value.append(item)
        else:
            self.max_value.append(max_val)

    def pop(self):
        if self.index == 0:
            return print("error")
        self.index -= 1
        self.items.pop()
        self.max_value.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def load_data():
    file = open("./input.txt", "rt")
    commands_len = int(file.readline().strip())
    commands = [x for x in file.read().split("\n")]
    stack = Stack()
    for command in commands:
        stack_interface(command, stack)


def stack_interface(data: str, stack: Stack):
    command = data.split()
    length = len(command)
    if length > 1:
        stack.COMMAND[data.split()[0]](int(data.split()[1]))
    elif length == 1:
        stack.COMMAND[data.split()[0]]()


if __name__ == '__main__':
    load_data()
    # import timeit
    #
    # print(timeit.timeit("load_data()", number=1000, setup="from __main__ import load_data"))
