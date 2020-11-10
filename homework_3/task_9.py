# Найти максимальный элемент среди минимальных элементов столбцов матрицы

import random

NUM_OF_COL = 4
NUM_OF_LEN = 3
MIN_ITEM = 1
MAX_ITEM = 10
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(NUM_OF_COL)] for _ in range(NUM_OF_LEN)]

maximum = 'max'

for x in range(len(matrix)):
    print(matrix[x])

for i in range(len(matrix[0])):
    minimum = matrix[0][i]
    for j in range(len(matrix)):
        if matrix[j][i] < minimum:
            minimum = matrix[j][i]

    if maximum == 'max':
        maximum = minimum
    elif minimum > maximum:
        maximum = minimum

print(f'Максимальный элемент среди минимальных: {maximum}')
