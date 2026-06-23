U = [
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
]
D = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
]
L = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0],
    [0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
]
R = [
    [0, 0, 0, 0, 0, 0, 0, 2],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 3, 0, 0, 0],
]
F = [
    [0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3],
    [2, 0, 0, 0, 0, 0, 0, 0],
]
B = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
]


def multiply_on_four(a, b):
    mapping = [
        [0, 0, 0, 0],
        [0, 1, 2, 3],
        [0, 2, 3, 1],
        [0, 3, 1, 2],
    ]
    return mapping[a][b]


def inverse_element_on_four(a):
    mapping = [0, 1, 3, 2]
    return mapping[a]


def inverse_matrix(matrix):
    n = len(matrix)
    aug = []
    for i in range(n):
        identity_row = [1 if i == j else 0 for j in range(n)]
        aug.append(matrix[i][:] + identity_row)
    for i in range(n):
        pivot_row = i
        while pivot_row < n and aug[pivot_row][i] == 0:
            pivot_row += 1
        if pivot_row == n:
            raise ValueError("逆行列が存在しません（正則行列ではありません）")
        if pivot_row != i:
            aug[i], aug[pivot_row] = aug[pivot_row], aug[i]
        pivot_val = aug[i][i]
        inv_pivot = inverse_element_on_four(pivot_val)
        for j in range(2 * n):
            aug[i][j] = multiply_on_four(aug[i][j], inv_pivot)
        for k in range(n):
            if k != i:
                factor = aug[k][i]
                if factor != 0:
                    for j in range(2 * n):
                        term = multiply_on_four(factor, aug[i][j])
                        aug[k][j] ^= term
    inv_matrix = [row[n:] for row in aug]
    return inv_matrix


def multiply_matrix(matrix1, matrix2):
    buffer = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                buffer[i][j] ^= multiply_on_four(matrix1[i][k], matrix2[k][j])
    return buffer


def square_matrix(matrix):
    return multiply_matrix(matrix, matrix)


def multiply_matrix_in_list(matrix_list):
    result = matrix_list[-1]
    for matrix in reversed(matrix_list[:-1]):
        result = multiply_matrix(matrix, result)
    return result


# g = [
#     square_matrix(B),
#     square_matrix(R),
# ]
# g = [
#     square_matrix(D),
#     square_matrix(B),
#     inverse_matrix(D),
#     square_matrix(F),
#     D,
#     square_matrix(B),
#     inverse_matrix(D),
#     square_matrix(F),
#     inverse_matrix(D),
# ]

P1 = [
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 3, 0, 0],
]

p2 = [
    multiply_matrix_in_list(
        [
            multiply_matrix(R, F),
            U,
            multiply_matrix(R, F),
            inverse_matrix(U),
        ]
    ),
    square_matrix(
        multiply_matrix_in_list(
            [
                multiply_matrix(L, F),
                U,
                multiply_matrix(L, F),
                inverse_matrix(U),
            ]
        ),
    ),
    multiply_matrix_in_list(
        [
            multiply_matrix(U, R),
            inverse_matrix(B),
            multiply_matrix(U, R),
            B,
        ]
    ),
    square_matrix(
        multiply_matrix_in_list(
            [
                multiply_matrix(L, F),
                U,
                multiply_matrix(L, F),
                inverse_matrix(U),
            ]
        ),
    ),
    square_matrix(
        multiply_matrix_in_list(
            [
                multiply_matrix(D, R),
                inverse_matrix(B),
                multiply_matrix(D, R),
                B,
            ]
        ),
    ),
    multiply_matrix_in_list(
        [
            multiply_matrix(R, B),
            D,
            multiply_matrix(R, B),
            inverse_matrix(D),
        ]
    ),
    multiply_matrix_in_list(
        [
            multiply_matrix(D, R),
            inverse_matrix(B),
            multiply_matrix(D, R),
            B,
        ]
    ),
    multiply_matrix_in_list(
        [
            multiply_matrix(U, R),
            inverse_matrix(B),
            multiply_matrix(U, R),
            B,
        ]
    ),
    square_matrix(
        multiply_matrix_in_list(
            [
                multiply_matrix(L, F),
                U,
                multiply_matrix(L, F),
                inverse_matrix(U),
            ]
        ),
    ),
    multiply_matrix_in_list(
        [
            multiply_matrix(L, B),
            D,
            multiply_matrix(L, B),
            inverse_matrix(D),
        ]
    ),
    U,
]
P2 = multiply_matrix_in_list(p2)

G = multiply_matrix(P2, P1)

for row in G:
    print(row)
