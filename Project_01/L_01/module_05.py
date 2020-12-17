
proceeds = float
costs = float
profit = float
roi = float
staff = int
proceeds_staff = float

print("Урок 1. Пункт 5")

proceeds = float(input("Введите, пожалуйста, выручку фирмы: "))
costs = float(input("Введите, пожалуйста, издержки фирмы: "))

if proceeds > costs:
    profit = proceeds - costs
    print(f"Фирма работает с прибылью {profit}")
    roi = profit / proceeds
    print(f"Соотношение прибыли и выручки {roi}")
    staff = int(input("Сообщите, пожалуйста, количество сотрудников фирмы: "))
    proceeds_staff = profit / staff
    print(f"Прибыль фирмы в рассчёте на одного сотрудника {proceeds_staff}")
else:
    print("Фирма работает с убытком")