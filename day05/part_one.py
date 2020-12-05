from decoder import get_id


with open("data.txt", "r") as f:
    codes = [code.replace('\n', '') for code in f.readlines()]

ids = [get_id(code) for code in codes]

print(max(ids))
