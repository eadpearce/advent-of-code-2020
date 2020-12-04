import pytest
from day04.parser import convert_to_dict
from day04.serializers import PassportSerializer


@pytest.mark.parametrize(
    'data',
    [
        "pid:0704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",  # pid too short
        "pid:087499709994 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",  # pid too long
        "pid:slfkdj hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",  # pid non-numeric
        "pid:087499709 hgt:740000in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",  # height too big
        "pid:087499709 hgt:djj4kin ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",  # height invalid format
        "pid:087499709 hgt:djj4kcm ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",  # height invalid format
        "pid:087499709 hgt:cmdjj4k ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",  # height invalid format
        "pid:087499709 hgt:indjj4k ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",  # height invalid format
        "pid:087499709 hgt:7cm ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",  # height too small
        "pid:087499709 hgt:170cm ecl:foo iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",  # ecl invalid choice
        "pid:087499709 hgt:170cm ecl:grn iyr:0 eyr:2030 byr:1980 hcl:#623a2f",  # iyr too small
        "pid:087499709 hgt:170cm ecl:grn iyr:3000 eyr:2030 byr:1980 hcl:#623a2f",  # iyr too big
        "pid:087499709 hgt:170cm ecl:grn iyr:2012 eyr:1 byr:1980 hcl:#623a2f",  # eyr too small
        "pid:087499709 hgt:170cm ecl:grn iyr:2012 eyr:4000 byr:1980 hcl:#623a2f",  # eyr too big
        "pid:087499709 hgt:170cm ecl:grn iyr:2012 eyr:2030 byr:1 hcl:#623a2f",  # byr too small
        "pid:087499709 hgt:170cm ecl:grn iyr:2012 eyr:2030 byr:5000 hcl:#623a2f",  # iyr too big
        "pid:087499709 hgt:170cm ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#sdflkj",  # hcl invalid
    ]
)
def test_serializer_invalid_data(data):
    passport = convert_to_dict(data)
    serializer = PassportSerializer(data=passport)
    assert not serializer.is_valid()


@pytest.mark.parametrize(
    'data',
    [
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
        "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
    ]
)
def test_serializer_valid_data(data):
    passport = convert_to_dict(data)
    serializer = PassportSerializer(data=passport)
    assert serializer.is_valid()
