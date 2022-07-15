rows, columns = [int(x) for x in input().split(', ')]

matrix = []
sum_matrix_nums = 0
for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    sum_matrix_nums += sum(row)
    matrix.append(row)
print(sum_matrix_nums)
print(matrix)


