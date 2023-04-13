def factorial(n: int, k: int) -> int:
    acc: int = 0
    prev: int = 0
    index: int = 0
    mod: int = 10**k
    if n == 1 or n == 0:
        return 1
    while index < n:
        if index == 0 or index == 1:
            acc += 1
            prev = 1
        else:
            acc = (prev + acc) % mod
            prev = acc - prev
        index += 1
    return acc


def factorial2(n):
    acc = []
    if n == 1 or n == 0:
        return 1
    for x in range(n - 1):
        if x == 0 or x == 1:
            acc.append(1)
        else:
            acc.append(sum(acc[-2:]))
    return sum(acc) + 1


def load_data():
    data = open('./input.txt', 'rt').readline().split()
    number = int(data[0])
    mod = int(data[1])
    print(factorial(number, mod))


if __name__ == '__main__':
    load_data()
    # import timeit
    #
    # print(timeit.timeit('load_data()', number=1, setup='from __main__ import load_data'))
