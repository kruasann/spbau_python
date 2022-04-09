import numpy as np
from relations_generator import RelationsGenerator


def main(n, m):
    properties = np.zeros([4, 4], dtype=int)  # свойства

    for relation in RelationsGenerator(n, m):  # очередное отношение

        counts_row = [sum(relation[i]) for i in range(n)]  # количество единиц в каждой строке
        counts_column = [sum(relation[:, j]) for j in range(m)]  # количество единиц в каждом столбце

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

    return properties


if __name__ == "__main__":
    n, m = map(int, input("Enter the numbers of elements of domain and codomain sets: ").split())
    print(main(n, m))
