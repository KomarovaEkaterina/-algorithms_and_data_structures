# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве

import random

LEN_OF_ARR = 6
MIN_ITEM = -100
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(LEN_OF_ARR)]

pos = -1
maximum = 0

print(f'Массив: {arr}')

for i in range(len(arr)):
    if arr[i] < 0 and pos == -1:
        maximum = arr[i]
        pos = i
    elif 0 > arr[i] > arr[pos]:
        maximum = arr[i]
        pos = i

if pos == -1:
    print("В массиве нет отрицательных элементов")
else:
    print(f'Максимальный отрицательный элемент: {maximum} расположен на позиции {pos + 1}')  # Для удобства восприятия pos + 1
