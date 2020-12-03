
with open("data.txt", "r") as f:
    lines = [
        line.replace("-", " ").replace(":", "").replace("\n", "").split(" ")
        for line in f.readlines()
    ]

valid_passwords = []

for position1, position2, letter, password in lines:
    index1 = int(position1) - 1
    index2 = int(position2) - 1

    if password[index1] == letter and password[index2] != letter:
        valid_passwords.append(password)
    elif password[index1] != letter and password[index2] == letter:
        valid_passwords.append(password)

print(len(valid_passwords))
