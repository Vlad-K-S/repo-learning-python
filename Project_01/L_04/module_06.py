
from itertools import count, cycle

first_part_number = int
second_part_number = int
first_part_list = list
second_part_list = list
string_with_numbers = str
original_list = list

print("Урок 4. Пункт 6")
# Первая часть задания

first_part_number = int(input("Введите, пожалуйста, целое число от 1 до 10: "))
first_part_list = []
second_part_list = []
index = 0

for index in count(first_part_number):
    first_part_list.append(index)
    if index == 10:
        break

print(first_part_list)

# Вторая часть задания
string_with_numbers = input("Введите, пожалуйста, строку значений, разделённых пробелами: ")
original_list = string_with_numbers.split(" ")
len_original_list = len(original_list)
second_part_number = int(input(f"Введите, пожалуйста, номер позиции, до которой выводим список"
                               f" - это целое число от 1 до {len_original_list}: "))
# Выше спрашиваем и получаем значения, преобразуем в лист
# Спрашиваем и получаем номер позиции, на который перестать выводить список

second_part_list = []
count = 1

for item in cycle(original_list):
    if count > second_part_number:
        break
    second_part_list.append(item)
    count = count + 1

print(second_part_list)





