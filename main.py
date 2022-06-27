def create_i_by_size(size):
    mtrx = []
    for i in range(size):
        mtrx.append([])
        for j in range(size):
            mtrx[i].append(0)
    for i in range(size):
        mtrx[i][i] = 1
    return mtrx

def solve_this(matrix,size):
    for i in range(size):
        pivot = abs(matrix[i][i])
        max_rox = i
        row = i+1
        while row<size:
            if abs(matrix[row][i] > pivot):
                pivot = abs(matrix[row][i])
                max_rox = row
            row += 1
        matrix = swap_rows(matrix, i, max_rox, size)
        matrix = set_pivot(matrix, i, i, size)
        row = i + 1
        while row < size:
            matrix = null_this(matrix, row, i, size, matrix[i][i])
            row += 1
    for i in range(1, size):
        row = i - 1
        while row >=0:
            matrix = null_this(matrix, row, i, size, matrix[i][i])
            row -= 1
    return matrix

def null_this(matrix, x, y, size, pivot):
    i_matrix = create_i_by_size(size)
    return matrix_multiply(edit_this(i_matrix, x, y, -1*matrix[x][y]/pivot), matrix)


def set_pivot(matrix,a,b,size):
    i_matrix = create_i_by_size(size)
    return matrix_multiply(edit_this(i_matrix, a, b, 1/matrix[a][b]), matrix)


def edit_this(matrix, a, b, value):
    matrix[a][b] = value
    return matrix


def matrix_multiply(a, b):  # A function that calculates the multiplication of 2 matrices and returns the new matrix
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    if cols_a != rows_b:
        print('Number of A columns must equal number of B rows.')
    new_matrix = []
    while len(new_matrix) < rows_a:  # while len small the len rows
        new_matrix.append([])  # add place
        while len(new_matrix[-1]) < cols_b:
            new_matrix[-1].append(0.0)  # add value
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]  # mul mat
            new_matrix[i][j] = total
    return new_matrix  # return the A*B=new matrix


def swap_rows(matrix,row_1,row_2,size):
    i_matrix = create_i_by_size(size)
    i_matrix[row_1],i_matrix[row_2] = i_matrix[row_2],i_matrix[row_1]
    return matrix_multiply(i_matrix,matrix)


def cubic_spline_interpolation(requested_p, x_vectors, y_vectors):
    gamma = []
    h = []
    d = []
    m_u = []

    for i in range(0, len(x_vectors) - 1):
        h.append(x_vectors[i + 1] - x_vectors[i])
    for i in range(1, len(x_vectors) - 1):
        gamma.append(h[i]/(h[i] + h[i - 1]))
        m_u.append(1 - h[i]/(h[i] + h[i - 1]))
        d.append((6 / (h[i] + h[i - 1]) * ((y_vectors[i + 1] - y_vectors[i]) / h[i] - (y_vectors[i] - y_vectors[i - 1]) / h[i - 1])))

    mtrx = create_i_by_size(len(d))
    for i in range(len(d)):
        mtrx[i][i] = 2
        if i != 0:
            mtrx[i][i-1] = m_u[i]
        if i != len(d)-1:
            mtrx[i][i+1] = gamma[i]
        mtrx[i].append(d[i])

    m = [0]
    result = solve_this(mtrx,len(d))
    for x in range(len(result) - 1):
        m.append(result[x][-1])
    m.append(0)
    print("Matrix =", mtrx)
    for y in range(len(y_vectors) - 1):
        if requested_p > x_vectors[y]:
            if requested_p < x_vectors[y + 1]:
                 print("f(x)=", ((x_vectors[y + 1] - requested_p) ** 3 * m[y] + (requested_p - x_vectors[y]) ** 3 * m[y + 1]) / (6 * h[y]) \
                       + ((x_vectors[y+1] - requested_p) * y_vectors[y] + (requested_p - x_vectors[y]) * y_vectors[y + 1]) / (h[y]) \
                       - h[y] * ((x_vectors[y + 1] - requested_p) * m[y] + (requested_p - x_vectors[y]) * m[y + 1]) / 6)



xVectors_Hackaton = [1,2,3,4,5]
yVectors_Hackaton = [0,1,0,1,0]

cubic_spline_interpolation(1.5,xVectors_Hackaton,yVectors_Hackaton)