import re
from rest_framework import serializers


class PassportSerializer(serializers.Serializer):
    byr = serializers.IntegerField(min_value=1920, max_value=2002)  # birth year
    iyr = serializers.IntegerField(min_value=2010, max_value=2020)  # issue year
    eyr = serializers.IntegerField(min_value=2020, max_value=2030)  # expiration year
    hgt = serializers.CharField()  # height
    ecl = serializers.CharField()  # eye colour
    hcl = serializers.CharField(min_length=7, max_length=7)  # hair colour
    pid = serializers.CharField(min_length=9, max_length=9)  # passport ID
    cid = serializers.CharField(required=False)  # country ID

    def validate_hgt(self, value):
        num, unit = 0, None

        try:
            num, unit = int(value[0:-2]), value[-2:]
        except ValueError:
            raise serializers.ValidationError('Invalid height format')

        if unit == 'cm':
            if num >= 150 and num <= 193:
                return value
            else:
                raise serializers.ValidationError('Height must be between 150 and 193')

        elif unit == 'in':
            if num >= 59 and num <= 76:
                return value
            else:
                raise serializers.ValidationError('Height must be between 59 and 76')
        else:
            raise serializers.ValidationError('Invalid height')

    def validate_ecl(self, value):
        choices = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value not in choices:
            raise serializers.ValidationError('Eye colour must be one of: amb, blu, brn, gry, grn, hzl, oth')
        return value

    def validate_pid(self, value):
        exp = re.compile(r'\d+')
        if not exp.match(value):
            raise serializers.ValidationError('Passport ID must be a nine-digit number')
        return value

    def validate_hcl(self, value):
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value)
        if not match:
            raise serializers.ValidationError('Hair colour must be a valid hex code')
        return value
