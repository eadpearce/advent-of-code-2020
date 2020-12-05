
id = 'FBFBBFFRLR'
rows = [i for i in range(0, 128)]
cols = [i for i in range(0, 8)]

for char in id[:7]:
    if char == 'F':
        rows = rows[:len(rows) // 2]  # low
    elif char == 'B':
        rows = rows[len(rows) // 2:]  # high

    if len(rows) == 1:
        print(f'Row: {rows[0]}')

for char in id[-3:]:
    if char == 'L':
        cols = cols[:len(cols) // 2]  # low
    elif char == 'R':
        cols = cols[len(cols) // 2:]  # high

    if len(cols) == 1:
        print(f'Column: {cols[0]}')

id = rows[0] * 8 + cols[0]
print(f'ID: {id}')
