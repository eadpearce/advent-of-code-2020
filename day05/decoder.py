
low = ['F', 'L']
high = ['B', 'R']


def split(seats, char):
    if char in low:
        return seats[:len(seats) // 2]
    elif char in high:
        return seats[len(seats) // 2:]


def get_id(code):

    rows, cols = get_coords(code)

    return rows * 8 + cols


def get_coords(code):

    rows = [i for i in range(0, 128)]
    cols = [i for i in range(0, 8)]

    for char in code[:7]:
        rows = split(rows, char)

    for char in code[-3:]:
        cols = split(cols, char)

    return (rows[0], cols[0])
