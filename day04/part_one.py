from parser import parse

passports = parse('data.txt')

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
