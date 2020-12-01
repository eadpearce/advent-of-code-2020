import math
from itertools import combinations


def main():
    with open("data.txt", "r") as f:
        number_list = [int(num) for num in f.readlines()]

    for i in combinations(number_list, 3):
        if sum(i) == 2020:
            print(list(i))
            print(math.prod(i))


if __name__ == '__main__':
    main()
