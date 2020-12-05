from decoder import get_coords, get_id


with open("data.txt", "r") as f:
    codes = [code.replace('\n', '') for code in f.readlines()]

rows = list(set([get_coords(code)[0] for code in codes]))
cols = list(set([get_coords(code)[1] for code in codes]))

seats = sorted([get_id(code) for code in codes])

my_id = [
    seats[i] + 1
    for i in range(len(seats) - 1)
    if seats[i + 1] - seats[i] == 2
]

print(my_id)
