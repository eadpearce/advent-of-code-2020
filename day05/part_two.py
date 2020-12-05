from decoder import get_id


with open("data.txt", "r") as f:
    codes = [code.replace('\n', '') for code in f.readlines()]

seats = sorted([get_id(code) for code in codes])

my_id = [
    seats[i] + 1
    for i in range(len(seats) - 1)
    if seats[i + 1] - seats[i] == 2
]

print(my_id)
