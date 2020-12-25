
from functools import reduce

print("Урок 4. Пункт 5")

new_list = []

for item in range(100, 1001):
    if (item % 2) == 0:
        new_list.append(item)


def sum_x_y(x, y):
    return x * y


result = reduce(sum_x_y, new_list)

print(result)
