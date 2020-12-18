
print("Урок 3. Пункт 3")


def my_func():
    var_1 = float(input("Введите, пожалуйста, число: "))
    var_2 = float(input("Введите, пожалуйста, число: "))
    var_3 = float(input("Введите, пожалуйста, число: "))
    sum_result = sum([var_1, var_2, var_3]) - min(var_1, var_2, var_3)
    return sum_result


print(f"Сумма двух наибольших чисел: {my_func()}")
