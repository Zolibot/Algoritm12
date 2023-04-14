def factorial(n):
    acc = []
    if n == 1 or n == 0:
        return 1
    for x in range(n - 1):
        if x == 0 or x == 1:
            acc.append(1)
        else:
            acc.append(sum(acc))
    return sum(acc)


def factorial1(n):
    if n == 1 or n == 0:
        return 1
    return factorial1(n - 1) + factorial1(n - 2)


def load_data():
    file = open('./input.txt', 'rt')
    number = int(file.readline().strip())
    print(factorial1(number))


if __name__ == '__main__':
    load_data()
    # import timeit
    #
    # print(timeit.timeit('load_data()', number=1000, setup='from __main__ import load_data'))
