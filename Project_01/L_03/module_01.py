
print("Урок 3. Пункт 1")


def divide_action ():
    dividend = float(input("Введите, пожалуйста, делимое: "))
    divider = float(input("Введите, пожалуйста, делитель: "))
    if divider == 0:
        result = "Введён делитель, равный нулю, выполнение функции невозможно."
    else:
        result = dividend / divider
    return result


print(f"Результат деления: {divide_action()}")
