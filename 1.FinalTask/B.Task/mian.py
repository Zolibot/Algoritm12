class Stack:
    def __init__(self):
        self.items = []
        self.index = 0

    def push(self, item):
        self.index += 1
        self.items.append(item)

    def pop(self):
        if self.index == 0:
            return "error"
        self.index -= 1
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def load_data():
    file = open("./input.txt", "rt")
    data = [x for x in file.read().split()]
    stack = Stack()
    operand = {'/': '//', '*': '*', '+': '+', '-': '-'}
    for x in data:
        if x not in operand:
            stack.push(x)
        else:
            first = str(stack.pop())
            second = str(stack.pop())
            s = second + operand[x] + first
            a = eval(s)
            stack.push(a)
    print(stack.peek())


if __name__ == "__main__":
    load_data()