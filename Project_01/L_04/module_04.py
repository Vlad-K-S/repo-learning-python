
original_list = list
new_list = list

print("Урок 4. Пункт 4")

original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []

for item in original_list:
    if original_list.count(item) == 1:
        new_list.append(item)

print(original_list)
print(new_list)
