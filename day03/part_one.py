
def main():
    with open("data.txt", "r") as f:
        mountain = f.readlines()

    trees = 0
    x = 0  # horizontal
    y = 0  # vertical
    x_end = len(mountain[0]) - 1
    y_end = len(mountain) - 1

    while True:
        x = (x + 3) % x_end

        y += 1

        if y == y_end:
            break

        # so i can see what the heck i am doing
        if mountain[y][x] == '#':
            line = mountain[y][:x] + 'X' + mountain[y][x+1:]
            trees += 1
        elif mountain[y][x] == '.':
            line = mountain[y][:x] + 'O' + mountain[y][x+1:]

        print(line)

    print(trees)


if __name__ == '__main__':
    main()
