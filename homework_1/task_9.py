a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a > b:
    if c > a:
        sr = a
    elif c > b:
        sr = c
    else:
        sr = b
else:
    if c > b:
        sr = b
    elif a > c:
        sr = a
    else:
        sr = c

print(f"Среднее число: {sr}")



