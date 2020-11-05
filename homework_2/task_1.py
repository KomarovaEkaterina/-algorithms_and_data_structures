znak = input("Введите знак операции: ")

while znak != '0':
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    if znak == '/':
        if b == 0:
            res = "Ай яй яй! Нельзя делить на 0"
        else:
            res = a / b
    elif znak == '*':
        res = a * b
    elif znak == '-':
        res = a - b
    elif znak == '+':
        res = a + b
    else:
        res = "Это не похоже на знак! Попробуй ввести снова."

    print(res)
    znak = input("Введите знак операции или 0 для выхода из программы: ")
