def factorial(n):
    acc = []
    if n == 1 or n == 0:
        return 1
    for x in range(n - 1):
        if x == 0 or x == 1:
            acc.append(1)
        else:
            acc.append(sum(acc[-2:]))
    return sum(acc) + 1


def factorial1(n):
    if n == 1 or n == 0:
        return 1
    return factorial1(n - 1) + factorial1(n - 2)


def load_data():
    file = open('./input.txt', 'rt')
    data = file.readline().split()
    number = int(data[0])
    mod = int(data[1])
    print(factorial(number) % (10**mod))


if __name__ == '__main__':
    load_data()
    # import timeit
    #
    # print(timeit.timeit('load_data()', number=1000, setup='from __main__ import load_data'))
