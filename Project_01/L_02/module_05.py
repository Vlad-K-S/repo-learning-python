
list_rating = list
new_rating = int

list_rating = [7, 5, 3, 3, 2]

print("Урок 2. Пункт 5")

print(f"Список значений рейтинга: {list_rating}")

new_rating = int(input("Введите, пожалуйста, целое положительное число для пополнения рейтинга:"))
list_rating.append(new_rating)
list_rating.sort(reverse=True)

print(f"Список значений рейтинга: {list_rating}")
