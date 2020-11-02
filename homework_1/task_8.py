year = int(input("Введите год: "))

if year % 4 == 0:
    res = "Год високосный"
else:
    res = "Год не високосный"

print(res)