matrix = [
    [7, 1, 3, 2, 1],
    [1, 3, 9, 8, 5],
    [4, 6, 7, 9, 1],
    [7, 1, 3, 3, 2],
    [1, 3, 9, 8, 5],
]
n = len(matrix)
print(f'Primary diagonal: {[matrix[i][i] for i in range(n)]}')
print(f'Secondary diagonal: {[matrix[i][n-i-1] for i in range(n)]}')
#print(f'Secondary diagonal: {[matrix[i][-i-1] for i in range(n)]}')
below_primary_diagonal = []
for r in range(n):
    for c in range(r):
        below_primary_diagonal.append(matrix[r][c])