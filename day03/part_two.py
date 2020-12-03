import math

with open("data.txt", "r") as f:
    mountain = f.readlines()

total_trees = 0

x_end = len(mountain[0]) - 1
y_end = len(mountain) - 1


def get_slope_trees(steps_right, steps_down):
    x = 0  # horizontal
    y = 0  # vertical
    trees = 0

    while True:
        x = (x + steps_right) % x_end

        y += steps_down

        if y == y_end:
            break

        if mountain[y][x] == '#':
            trees += 1

    return trees


answer = math.prod([
    get_slope_trees(1, 1),
    get_slope_trees(3, 1),
    get_slope_trees(5, 1),
    get_slope_trees(7, 1),
    get_slope_trees(1, 2),
])

print(answer)
