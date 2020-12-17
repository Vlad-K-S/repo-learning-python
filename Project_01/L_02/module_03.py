
item = int
number_month = int
dict_year = dict
list_winter_el = list
list_summer_el = list
list_spring_el = list
list_fall_el = list

list_winter_el = [12, 1, 2]
list_summer_el = [6, 7, 8]
list_spring_el = [3, 4, 5]
list_fall_el = [9, 10, 11]
dict_year = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна",
             6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}

print("Урок 2. Пункт 3")

number_month = int(input("Введите, пожалуйста, месяц в виде целого числа от 1 до 12:"))

print(f"Месяц {number_month} - это сезон {dict_year.get(number_month)}")

number_month = int(input("Введите, пожалуйста, месяц в виде целого числа от 1 до 12:"))

if list_winter_el.count(number_month) > 0:
    print(f"Месяц {number_month} - это сезон Зима")
elif list_summer_el.count(number_month) > 0:
    print(f"Месяц {number_month} - это сезон Лето")
elif list_spring_el.count(number_month) > 0:
    print(f"Месяц {number_month} - это сезон Весна")
elif list_fall_el.count(number_month) > 0:
    print(f"Месяц {number_month} - это сезон Осень")
else:
    print("К сожалению, Вы ввели некорректное число")
