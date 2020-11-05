a = int(input("Введите число: "))
new = ''

while a != 0:
    new += str(a % 10)
    a = a // 10

print(f"Число перевртыш - {int(new)}")
