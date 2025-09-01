rows = 3
cols = 3
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"element at ({i},{j}): "))
        row.append(value)
    matrix.append(row)
for row in matrix:
    print(row)