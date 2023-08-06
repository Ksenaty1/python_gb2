def transpose(matrix: dict):
    return [list(row) for row in zip(*matrix)]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))