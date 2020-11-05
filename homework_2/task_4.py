def count_sum(a, b):
    if b == 0:
        return 0
    else:
        return a + count_sum(a / -2, b - 1)


n = int(input("Введите количество элементов ряда, которые собираетесь сложить: "))

res = count_sum(1, n)

print(f"Сумма ровна: {res}")
