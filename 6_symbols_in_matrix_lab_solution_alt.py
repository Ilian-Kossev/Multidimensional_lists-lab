n = int(input())
matrix = []
for num in range(n):
    row = input()
    matrix.append(row)
symbol = input()

row, col = None, None
is_found = True
for r in range(len(matrix)):
    if symbol in matrix[r]:
        row = r
        col = matrix[r].index(symbol)
        is_found = True
        break
if is_found:
    print(f'({row}, {col})')
else:
    print(f"{symbol} does not occur in the matrix")

