rows, columns = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

result = 0
for column_index in range(columns):
    for row_index in range(rows):
        number_to_add = matrix[row_index][column_index]
        result += number_to_add
    print(result)
    result = 0