import pytest
from day04.parser import parse, parse_file


@pytest.mark.parametrize(
    'filename,length',
    [
        ('./tests/testdata/four.txt', 4),
        ('./tests/testdata/two.txt', 2),
        ('./tests/testdata/three.txt', 3),
    ]
)
def test_parser(filename, length):
    string = parse_file(filename)
    data = parse(string)
    assert len(data) == length
