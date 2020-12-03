
with open("data.txt", "r") as f:
    number_list = [int(num) for num in f.readlines()]

for num_one in number_list:
    for num_two in number_list:
        total = num_one + num_two
        if total == 2020:
            print(total)
            print(num_one, num_two)
            print(num_one * num_two)
