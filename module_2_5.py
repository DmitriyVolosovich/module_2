def get_matrix(n, m, value):
    matrix = []
    void = []
    if m <= 0 or n <= 0 or value <= 0:
        return matrix
    else:
        for i in range(n):
            i += 1
            matrix.append(void)
        for j in range(m):
            j += 1
            void.append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)