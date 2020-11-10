# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться

import random

LEN_OF_ARR = 6
MIN_ITEM = 1
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(LEN_OF_ARR)]

first_min = arr[0]
second_min = arr[1]

print(f'Массив: {arr}')

for i in range(LEN_OF_ARR):
    if arr[i] < first_min:
        second_min = first_min
        first_min = arr[i]
    elif arr[i] <= second_min:
        second_min = arr[i]

print(f'Первый минимальный элемент: {first_min}\nВторой минимальный элемент: {second_min}')
