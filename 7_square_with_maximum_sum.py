rows, cols = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

new_matrix_first = []
new_matrix_second = []
biggest_result = 0
result = 0
for r in range(rows-1):
    for c in range(cols-1):
        result = matrix[r][c] + matrix[r+1][c] + matrix[r][c+1] + matrix[r+1][c+1]
        if result > biggest_result:
            biggest_result = result
            new_matrix_first = [matrix[r][c], matrix[r][c+1]]
            new_matrix_second = [matrix[r+1][c], matrix[r+1][c+1]]


print(' '.join(str(x) for x in new_matrix_first))
print(' '.join(str(x) for x in new_matrix_second))
print(biggest_result)

