from typing import Dict


class Stack:
    def __init__(self):
        self.items = []
        self.index = 0

    def push(self, item):
        self.index += 1
        self.items.append(item)

    def pop(self):
        if self.index == 0:
            return None
        self.index -= 1
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return self.index


def load_data() -> None:
    file = open("./input.txt", "rt")
    print(is_correct_bracket_seq(file.readline()))


def is_correct_bracket_seq(data: str) -> bool:
    stack: Stack = Stack()
    bk: Dict = {'[': ']', '{': '}', '(': ')'}
    for bra in data:
        if bra in bk.keys():
            stack.push(bra)
            continue
        if bra in bk.values():
            if stack.size() == 0:
                return False
            if bk[stack.peek()] == bra:
                stack.pop()
            else:
                return False

    return True


if __name__ == '__main__':
    load_data()
    # import timeit
    #
    # print(timeit.timeit("load_data()", number=10, setup="from __main__ import load_data"))
