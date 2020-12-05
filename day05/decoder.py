
low = ['F', 'L']
high = ['B', 'R']


def get_id(code):
    rows = [i for i in range(0, 128)]
    cols = [i for i in range(0, 8)]

    for char in code[:7]:
        if char in low:
            rows = rows[:len(rows) // 2]
        elif char in high:
            rows = rows[len(rows) // 2:]

    for char in code[-3:]:
        if char in low:
            cols = cols[:len(cols) // 2]
        elif char in high:
            cols = cols[len(cols) // 2:]

    return rows[0] * 8 + cols[0]
