def read_matrix():
    n, m = [int(x) for x in input().split(', ')]
    # n, m = map(int, input().split(', '))

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)

    return matrix


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])
the_sum = 0

for row_index in range(n):
    row = matrix[row_index]
    the_sum += sum(row)
    #for column_index in range(m):
    #    the_sum += row[column_index]

print(the_sum)
# - кратък вариант: the_sum_2 = sum(sum(row) for row in matrix)

