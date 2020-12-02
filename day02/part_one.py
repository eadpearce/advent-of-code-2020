
def main():
    with open("data.txt", "r") as f:
        lines = [
            line.replace("-", " ").replace(":", "").replace("\n", "").split(" ")
            for line in f.readlines()
        ]

    valid_passwords = []

    for min, max, letter, password in lines:
        total = len([char for char in password if char == letter])
        if total >= int(min) and total <= int(max):
            valid_passwords.append(password)

    print(len(valid_passwords))


if __name__ == '__main__':
    main()
