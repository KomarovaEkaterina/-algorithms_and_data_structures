# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

LEN_OF_ARR = 6
MIN_ITEM = 1
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(LEN_OF_ARR)]

print(f'Начальный массив: {arr}')

for i in range(len(arr)):
    greatest = 0
    smallest = 0
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            greatest += 1
        if arr[i] > arr[j]:
            smallest += 1
    if greatest == 0:
        gr_pos = i
    if smallest == 0:
        sm_pos = i

tmp = arr[gr_pos]
arr[gr_pos] = arr[sm_pos]
arr[sm_pos] = tmp

print(f'Измененный массив: {arr}')
