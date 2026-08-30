#dot products of 2 vectors
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    
    return sum(a * b for a, b in zip(vector1, vector2))


# magnitude of a vector
def magnitude(vector):
    return sum(x ** 2 for x in vector) ** 0.5

# transpose of a matrix
def transpose(matrix):
    return [list(row) for row in zip(*matrix)] 

# multiplication of 2 matrices
def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))))
        result.append(row)
    
    return result