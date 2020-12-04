
def parse_file(filename):
    with open(filename, "r") as f:
        data = f.read()
    return [
        string.replace('\n', ' ')
        for string in data.split('\n\n')
    ]


def parse(strings):
    return [convert_to_dict(string) for string in strings]


def convert_to_dict(string):
    return dict([
        key_value_pair.split(':')
        for key_value_pair in string.split(' ')
        if key_value_pair
    ])
