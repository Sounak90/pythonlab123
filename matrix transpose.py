rows = 3
cols = 3
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"element at ({i},{j}): "))
        row.append(value)
    matrix.append(row)
print("")
print("My Matrix:")
for row in matrix:
    print(row)
print("")
transposed = []
for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transposed.append(new_row)
print("Transposed Matrix:")
for k in transposed:
    print(k)