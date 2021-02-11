
from sys import argv

script_name, work_hours, pay_hour, bonus = argv

print("Урок 4. Пункт 1")

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", work_hours)
print("Ставка в час: ", pay_hour)
print("Премия: ", bonus)

salary = (int(work_hours) * int(pay_hour)) + int(bonus)
# Зарплата = (выработка в часах * ставка в час) + премия

print(f"Зарплата: {salary}")
