
raise_wages = list
sum_wages = int
people = int

print("Урок 5. Пункт 3")

raise_wages = []
sum_wages = 0
people = 0

with open("file_3.txt", "r", encoding="utf-8") as file_to_read:
    for info_string in file_to_read:
        info_list = info_string.split()
        sum_wages = sum_wages + int(info_list[1])
        people = people + 1
        if int(info_list[1]) < 20000:
            raise_wages.append(info_list[0])

print(f"Средняя зарплата сотрудника: {sum_wages / people}")
print(f"Поднять зарплату сотрудникам: {raise_wages}")
