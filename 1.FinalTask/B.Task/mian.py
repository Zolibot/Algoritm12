# 85832684
from typing import List
from operator import add, sub, mul, floordiv

operators = {'/': floordiv, '*': mul, '+': add, '-': sub}


class EmptyStackError(Exception):
    def __init__(self):
        super().__init__('error')


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self) -> int:
        try:
            return self.items.pop()
        except EmptyStackError:
            raise EmptyStackError()


def load_data() -> List[str]:
    file = open('./input.txt', 'rt')
    cmd = file.read().split()
    return cmd


def polish_notation_processing(store: Stack, data: List[str]) -> None:
    for calc_input in data:
        if calc_input not in operators:
            store.push(calc_input)
        else:
            first, second = int(store.pop()), int(store.pop())
            result = operators[calc_input](second, first)
            store.push(result)


if __name__ == '__main__':
    commands = load_data()
    stack: Stack = Stack()
    polish_notation_processing(stack, commands)
    print(stack.pop())
