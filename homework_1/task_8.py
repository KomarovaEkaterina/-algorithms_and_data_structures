year = int(input("Введите год: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            res = "Год високосный"
        else:
            res = "Год не високосный"
    else:
        res = "Год високосный"
else:
    res = "Год не високосный"

print(res)
