
string_with_items = str
# Строка для входящих данных
list_with_items = list
# Список для входящих данных
length_list_with_items = int
# Длина полученного списка
new_list_with_items = list
# Новый список, в котором будет итоговое значение
index = int
# Счётчик для цикла и индекс для списка

print("Урок 2. Пункт 2")

string_with_items = input("Введите, пожалуйста, элементы списка, разделённые пробелом:")
list_with_items = string_with_items.split(" ")
# Получили значения в строку, превратили в список

print(f"Введённый список: {list_with_items}")

length_list_with_items = len(list_with_items)
# Получили количество элементов списка

index = 0
# Цикл нужно начать с нуля, так как это будет индекс
new_list_with_items = []
# Новый список будет наполняться, он должен быть пустой

if length_list_with_items > 0:
    while index < (length_list_with_items - 1):
        new_list_with_items.insert(index, list_with_items[index + 1])
        new_list_with_items.insert(index + 1, list_with_items[index])
        index = index + 2
    if length_list_with_items % 2 != 0:
        new_list_with_items.append(list_with_items[length_list_with_items - 1])
else:
    new_list_with_items = list_with_items.copy()
# Если в списке больше 1 элемента, проходим по нему, добавляя элементы в новый список в нужном порядке
# Если элементов нечётное количество, добавляем последний элемент в новый список
# Если в списке 1 элемент, новый список равен изначальному

print(f"Итоговый список: {new_list_with_items}")
