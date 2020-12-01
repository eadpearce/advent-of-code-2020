
def main():
    with open("data.txt", "r") as f:
        number_list = [int(num) for num in f.readlines()]

    for num_one in number_list:
        for num_two in number_list:
            for num_three in number_list:
                total = num_one + num_two + num_three
                if total == 2020:
                    print(num_one, num_two, num_three)
                    print(num_one * num_two * num_three)


if __name__ == '__main__':
    main()
