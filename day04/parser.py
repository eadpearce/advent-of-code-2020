
def parse(filename):
    with open(filename, "r") as f:
        data = f.read()

    return [
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
