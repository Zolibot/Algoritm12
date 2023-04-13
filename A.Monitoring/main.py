def load_data():
    data = open('./input.txt', 'rt').read().split("\n")
    row = [x.split() for x in data]
    i = int(row[0][0])
    j = int(row[1][0])
    arr = row[2:]

    for y in range(j):
        for x in range(i):
            print(arr[x][y], end=" ")
        print()


if __name__ == '__main__':
    load_data()
    # import timeit
    #
    # print(timeit.timeit('load_data()', number=1, setup='from __main__ import load_data'))
