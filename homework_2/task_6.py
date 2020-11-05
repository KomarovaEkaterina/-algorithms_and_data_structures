import random

num = random.randint(1, 100)
i = 0

while True:
    variant = int(input("Ваш вариант: "))

    if variant == num:
        print("Вы угадали! Круть)")
        break
    elif variant > num:
        print("Мимо! Надо было меньше...")
    else:
        print("Мимо! Надо было больше...")

    i += 1

    if i == 10:
        print("Вы проиграли :(")
        break
