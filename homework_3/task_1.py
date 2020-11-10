# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

START_DIVIDER = 2
END_DIVIDER = 9
START_NUM = 2
END_NUM = 99

for i in range(START_DIVIDER, END_DIVIDER + 1):
    res = 0
    for j in range(START_NUM, END_NUM + 1):
        if j % i == 0:
            res += 1
    print(f'{i} - {res}')
