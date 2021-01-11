
print("Урок 3. Пункт 4")

x = float(input("Введите, пожалуйста, x - действительное положительное число: "))
y = float(input("Введите, пожалуйста, y - целое отрицательное число: "))


def my_func1(x, y):
    index = int
    z = int
    index = 1
    z = 1
    result = float
    while index < (abs(y) + 1):
        z = z * x
        index = index + 1
    else:
        result = 1 / z
    return result


print(f"Результат возведения {x} в степень {y}: {my_func1(x, y)}")

x = float(input("Введите, пожалуйста, x - действительное положительное число: "))
y = float(input("Введите, пожалуйста, y - целое отрицательное число: "))


def my_func2(x, y):
    result = x ** y
    return result


print(f"Результат возведения {x} в степень {y}: {my_func2(x, y)}")
