import numpy as np

def vector_addition(x, y):
    if len(x) != len(y):
        return "Vectors must be the same length."
    new_vector = []
    for i in range(0, len(x)):
        new_vector.append(x[i] + y[i])

    return new_vector

def vector_subtraction(x, y):
    if len(x) != len(y):
        return "Vectors must be the same length."
    new_vector = []
    for i in range(0, len(x)):
        new_vector.append(x[i] - y[i])

    return new_vector

def scalar_mult_of_number_and_vector(number, x):

    new_vector = []
    for i in range(0, len(x)):
        new_vector.append(number * x[i])

    return new_vector

def L1_norm_of_vector(x):

    sum_of_abs_elements = 0
    for i in range(0, len(x)):
        sum_of_abs_elements += (np.abs(x[i]))

    return sum_of_abs_elements

def L2_norm_of_vector(x):

    sum_of_squared_elements = 0
    for i in range(0, len(x)):
        sum_of_squared_elements += (x[i]*x[i])

    norm = np.sqrt(sum_of_squared_elements)

    return norm

def Linf_norm_of_vector(x):

    max = x[0]
    for i in range(1, len(x)):
        if x[i] > max:
            max = x[i]

    return max

def dot_product(x, y):
    if len(x) != len(y):
        return "Vectors must be the same length."
    sum = 0
    for i in range(0, len(x)):
        sum += (x[i]*y[i])

    return sum

def cross_product(x, y):
    if len(x) != 3 or len(y) != 3:
        return "Vectors for triple product must have length of 3."
    if len(x) != len(y):
        return "Vectors must be the same length."
    new_vector = []

    new_vector.append(x[1]*y[2] - x[2]*y[1])
    new_vector.append(-(x[0]*y[2] - x[2]*y[0]))
    new_vector.append(x[0]*y[1] - x[1]*y[0])

    return new_vector

def triple_product(x, y, z):
    if len(x) != 3 or len(y) != 3:
        return "Vectors for cross product must have length of 3."
    if len(x) != len(y):
        return "Vectors must be the same length."

    sum = 0

    sum += x[0]*(y[1]*z[2] - y[2]*z[1])
    sum += x[1]*(-(y[0]*z[2] - y[2]*z[0]))
    sum += x[2]*(y[0]*z[1] - y[1]*z[0])

    return sum

def action_of_matrix_on_vector(a, u):
    for i in range(0, len(a)):
        if type(a[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    if len(a) != len(u):
        return "The # of columns of the matrix must be the same number of rows of the vector."
    new_vector = []
    for i in range(len(a)):
        sum = 0
        for j in range(len(u)):
            sum += a[i][j] * u[j]
        new_vector.append(sum)

    return new_vector

def sum_of_matrices(a, b):
    for i in range(0, len(a)):
        if type(a[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    for i in range(0, len(b)):
        if type(b[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    if len(a) != len(b):
        return "Matrices must have the same number of rows."
    for i in range(0, len(a)):
        if len(a[i]) != len(b[i]):
            return "Matrices must have the same number of columns."

    new_matrix = []

    for i in range(0, len(a)):
        new_row = []
        for j in range(0, len(a[i])):
            new_row.append(a[i][j] + b[i][j])
        new_matrix.append(new_row)

    return new_matrix


def difference_of_matrices(a, b):
    for i in range(0, len(a)):
        if type(a[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    for i in range(0, len(b)):
        if type(b[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    if len(a) != len(b):
        return "Matrices must have the same number of rows."
    for i in range(0, len(a)):
        if len(a[i]) != len(b[i]):
            return "Matrices must have the same number of columns."

    new_matrix = []

    for i in range(0, len(a)):
        new_row = []
        for j in range(0, len(a[i])):
            new_row.append(a[i][j] - b[i][j])
        new_matrix.append(new_row)

    return new_matrix

def product_of_matrices(a, b):

    # checking for lists
    for i in range(0, len(a)):
        if type(a[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    for i in range(0, len(b)):
        if type(b[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."

    if len(a[0]) != len(b) or len(b[0]) != len(a):
        return "The # of columns of the first matrix must equal the # of rows of the second matrix and vice versa."

    new_matrix = []

    for i in range(0, len(a)):
        new_row = []

        for j in range(0, len(a)):
            sum = 0
            for k in range(0, len(b)):
                sum += a[i][k]*b[k][j]
            new_row.append(sum)
        new_matrix.append(new_row)

    return new_matrix

def hadamard_product_of_matrices(a, b):

    # checking for lists
    for i in range(0, len(a)):
        if type(a[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."
    for i in range(0, len(b)):
        if type(b[i]) != list:
            return "The elements of the matrix must contain lists for it to be a matrix."

    if len(a[0]) != len(b[0]) or len(a) != len(b):
        return "The # of columns of the first matrix must equal the # of cols of the second matrix and same with number of rows."

    new_matrix = []

    for i in range(0, len(a)):
        new_row = []
        for j in range(0, len(b)):
            element = a[i][j]*b[i][j]
            new_row.append(element)
        new_matrix.append(new_row)

    return new_matrix