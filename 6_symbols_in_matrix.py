n = int(input())
matrix = []
for num in range(n):
    row = [x for x in input()]
    matrix.append(row)
symbol = input()

symbol_found = False
for r in range(n):
    for c in range(n):
        if matrix[r][c] == symbol:
            symbol_found = True
            print(f'({r}, {c})')
            break
    if symbol_found:
        break
if not symbol_found:
    print(f"{symbol} does not occur in the matrix")