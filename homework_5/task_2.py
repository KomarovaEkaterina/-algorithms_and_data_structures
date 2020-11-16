# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

from collections import deque


def count_sum(a, b, in_, out_):
    res_sum = deque()
    dop = 0
    while len(a) > 0:
        c = in_[a.pop()]
        d = in_[b.pop()]
        sum_ = c + d + dop

        if sum_ > 15:
            ost = sum_ - 16
            dop = 1
        else:
            ost = sum_
            dop = 0

        res_sum.appendleft(out_[ost])

        if len(a) == 0 and dop != 0:
            res_sum.appendleft(out_[dop])

    return res_sum


nums_in = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '0': 0}
nums_out = {value: key for key, value in nums_in.items()}

num_1 = deque(input("Введите первое число: ").upper())
num_2 = deque(input("Введите второе число: ").upper())

if len(num_1) > len(num_2):
    tmp = len(num_1) - len(num_2)
    num_2.extendleft('0' * tmp)
else:
    tmp = len(num_2) - len(num_1)
    num_1.extendleft('0' * tmp)

print(f"Сумма: {count_sum(num_1, num_2, nums_in, nums_out)}")




