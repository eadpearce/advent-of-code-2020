
with open("data.txt", "r") as f:
    data = f.read()

passports = [
    dict([
        key_value_pair.split(':')
        for key_value_pair in passport.split(' ')
        if key_value_pair
    ])
    for passport in [
        string.replace('\n', ' ')
        for string in data.split('\n\n')
    ]
]

required_keys = [
    'ecl',
    'pid',
    'eyr',
    'hcl',
    'byr',
    'iyr',
    'hgt',
    # 'cid', not this one!
]

valid_passports = []

for passport in passports:
    if all([key in passport for key in required_keys]):
        valid_passports.append(passport)

print(len(valid_passports))
