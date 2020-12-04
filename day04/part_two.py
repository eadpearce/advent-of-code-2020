from parser import parse_file, parse
from serializers import PassportSerializer
from constants import REQUIRED_KEYS


values = parse_file('data.txt')
passport_data = parse(values)

passports = [
    passport for passport in passport_data
    if all([key in passport for key in REQUIRED_KEYS])
]

valid = []
invalid = []

for passport in passports:
    serializer = PassportSerializer(data=passport)

    if serializer.is_valid():
        valid.append(serializer.validated_data)
        print(serializer.validated_data)
    else:
        invalid.append(serializer.validated_data)

print(len(valid))
