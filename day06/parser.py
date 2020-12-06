
def parse_file(filename):
    with open(filename, "r") as f:
        data = f.read()
    return [
        string.split('\n')
        for string in data.split('\n\n')
    ]


def parse(filename):
    return [
        list(''.join(string)) for string in parse_file(filename)
    ]
