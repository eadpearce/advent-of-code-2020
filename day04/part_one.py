from parser import parse_file, parse
from constants import REQUIRED_KEYS

values = parse_file('data.txt')
passports = parse(values)

valid_passports = []

for passport in passports:
    if all([key in passport for key in REQUIRED_KEYS]):
        valid_passports.append(passport)

print(len(valid_passports))
