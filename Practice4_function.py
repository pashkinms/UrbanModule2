def get_matrix(n = 2, m = 2, value = 0):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    return matrix

matrix = get_matrix(4, 5, 56)
print(matrix)