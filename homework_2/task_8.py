def count_enter(i, a, b):
    if b == 0:
        return 0
    else:
        chislo = input(f"{i}: ")
        return chislo.count(a) + count_enter(i + 1, a, b - 1)


x = input("Введите цифру, количество повторений которой планируете получить: ")
num = int(input(f"Введите количество чисел, в которых будем искать все {x}: "))

res = count_enter(1, x, num)

print(f"Количество {x} в введенных вами числах: {res}")
