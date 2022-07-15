rows = int(input())

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary_diagonal = [matrix[i][i] for i in range(rows)]
sum_primary_diagonal = sum(primary_diagonal)
print(sum_primary_diagonal)
