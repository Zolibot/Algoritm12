from collections import Counter
from typing import List


def load_data() -> None:
    file = open("./input.txt", "rt")
    print(is_correct_bracket_seq(file.readline()))


def is_correct_bracket_seq(data: str) -> bool:
    bracket_start: List[str] = [']', '}', ')']
    bracket_end: List[str] = ['[', '{', '(']
    count_bracket = Counter(data)
    for b1, b2 in zip(bracket_start, bracket_end):
        if count_bracket[b1] != count_bracket[b2]:
            return False
    return True


if __name__ == '__main__':
    load_data()
    # import timeit
    #
    # print(timeit.timeit("load_data()", number=1000, setup="from __main__ import load_data"))
