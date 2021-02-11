
from itertools import count
from math import factorial

print("Урок 4. Пункт 7")

factorial_number = int(input("Введите, пожалуйста, целое число, "
                             "для которого посчитаем факториал: "))

def fact(n):
    for item in count(1):
        if n >= item:
            yield factorial(item)
        else:
            break


for el in fact(factorial_number):
    print(f"Факториал: {el}")
