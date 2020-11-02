x = int(input("Ввведите целое трехзначное число: "))

a = x % 10
b = x % 100 // 10
c = x % 1000 // 100

res_sum = a + b + c
res_mult = a * b * c

print(f"Сумма цифр в числе: {res_sum}\nПроизведение цифр в числе: {res_mult}")
