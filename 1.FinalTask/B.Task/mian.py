# 85876108
from typing import List
from operator import add, sub, mul, floordiv

operators = {'/': floordiv, '*': mul, '+': add, '-': sub}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self) -> int:
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('pop from empty stack')


def load_data() -> List[str]:
    file = open('./input.txt', 'rt')
    cmd = [x if x in operators else int(x) for x in file.read().split()]
    return cmd


def calc_handle(data: List[str]) -> int:
    stack: Stack = Stack()
    for calc_input in data:
        if calc_input not in operators:
            stack.push(calc_input)
        else:
            first, second = stack.pop(), stack.pop()
            result = operators[calc_input](second, first)
            stack.push(result)
    return stack.pop()


if __name__ == '__main__':
    commands = load_data()
    msg = calc_handle(commands)
    print(msg)
