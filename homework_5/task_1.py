# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict


companies = defaultdict(float)
num = int(input("Введите колличество предприятий: "))
amount = 0

for i in range(num):
    name = input(f"Введите название {i + 1}-го предприятия: ")
    first = float(input("Введите прибыль за 1-й квартал: "))
    second = float(input("Введите прибыль за 2-й квартал: "))
    third = float(input("Введите прибыль за 3-й квартал: "))
    forth = float(input("Введите прибыль за 4-й квартал: "))

    sr_for_one = (first + second + third + forth) / 4
    amount += sr_for_one
    companies[name] = sr_for_one

sr_for_all = amount / num
more_sr = ''
less_sr = ''

for key, value in companies.items():
    # print(f"В компании {key} средняя прибыль {value}")
    if value > sr_for_all:
        more_sr += key + ' '
    elif value < sr_for_all:
        less_sr += key + ' '

print(f"Средняя прибыль по всем компаниям: {sr_for_all}")

print(f"Компания(и), заработавшие больше среднего: {more_sr}")
print(f"Компания(и), заработавшие меньше среднего: {less_sr}")




