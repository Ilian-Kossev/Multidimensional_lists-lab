rows, columns = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

column_sums = [0] * columns
for c in range(columns):
    for r in range(rows):
        value = matrix[r][c]
        column_sums[c] += value
[print(el) for el in column_sums]


