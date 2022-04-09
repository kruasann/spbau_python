from numba import njit, prange
import numpy as np
import time


@njit(fastmath=True)
def get_next(values, n, m):  # очередное отношение
    for i in prange(n):
        for j in range(m):
            if values[i][j] == 0:
                values[i][j] = 1
                return values

            values[i][j] = 0
    return np.array([[-1], [-1]])


@njit(fastmath=True)
def main(n, m):
    properties = np.array([[0] * 4] * 4)  # свойства
    relation = np.array([[0] * m] * n)  # матрица отношения

    while relation[0][0] != -1:
        counts_row = [sum(relation[i]) for i in np.arange(n)]  # количество единиц в каждой строке
        counts_column = [sum(relation[:, j]) for j in np.arange(m)]  # количество единиц в каждом столбце

        more_1_row, less_1_row = 0, 0
        for count in counts_row:
            if count >= 1:
                more_1_row += 1
            if count <= 1:
                less_1_row += 1

        more_1_col, less_1_col = 0, 0
        for count in counts_column:
            if count >= 1:
                more_1_col += 1
            if count <= 1:
                less_1_col += 1

        if (more_1_row == n) and (less_1_row == n) and (less_1_col < m) and (more_1_col < m):
            properties[0][0] += 1
        elif (more_1_row == n) and (less_1_row == n) and (less_1_col < m) and (more_1_col == m):
            properties[0][1] += 1
        elif (more_1_row == n) and (less_1_row < n) and (less_1_col < m) and (more_1_col == m):
            properties[0][2] += 1
        elif (more_1_row == n) and (less_1_row < n) and (less_1_col < m) and (more_1_col < m):
            properties[0][3] += 1

        elif (more_1_row == n) and (less_1_row == n) and (less_1_col == m) and (more_1_col < m):
            properties[1][0] += 1
        elif (more_1_row == n) and (less_1_row == n) and (less_1_col == m) and (more_1_col == m):
            properties[1][1] += 1
        elif (more_1_row == n) and (less_1_row < n) and (less_1_col == m) and (more_1_col == m):
            properties[1][2] += 1
        elif (more_1_row == n) and (less_1_row < n) and (less_1_col == m) and (more_1_col < m):
            properties[1][3] += 1

        elif (more_1_row < n) and (less_1_row == n) and (less_1_col == m) and (more_1_col < m):
            properties[2][0] += 1
        elif (more_1_row < n) and (less_1_row == n) and (less_1_col == m) and (more_1_col == m):
            properties[2][1] += 1
        elif (more_1_row < n) and (less_1_row < n) and (less_1_col == m) and (more_1_col == m):
            properties[2][2] += 1
        elif (more_1_row < n) and (less_1_row < n) and (less_1_col == m) and (more_1_col < m):
            properties[2][3] += 1

        elif (more_1_row < n) and (less_1_row == n) and (less_1_col < m) and (more_1_col < m):
            properties[3][0] += 1
        elif (more_1_row < n) and (less_1_row == n) and (less_1_col < m) and (more_1_col == m):
            properties[3][1] += 1
        elif (more_1_row < n) and (less_1_row < n) and (less_1_col < m) and (more_1_col == m):
            properties[3][2] += 1
        elif (more_1_row < n) and (less_1_row < n) and (less_1_col < m) and (more_1_col < m):
            properties[3][3] += 1

        relation = get_next(relation, n, m)

    return properties


if __name__ == "__main__":
    main(1, 1)  # для компиляции

    n, m = map(int, input("Enter the numbers of elements of domain and codomain sets: ").split())
    time0 = time.time()
    print(main(n, m))
    print(time.time() - time0)
