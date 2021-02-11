
original_list = list
new_list = list

print("Урок 4. Пункт 2")

original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []

for item in range(1, len(original_list)):
    if original_list[item] > original_list[item - 1]:
        new_list.append(original_list[item])

print(original_list)
print(new_list)
