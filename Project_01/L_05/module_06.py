
from re import findall

print("Урок 5. Пункт 6")
result = {}

with open("file_6.txt", "r", encoding="utf-8") as file_to_read:
    for info_string in file_to_read:
        hours = (findall('\d+', info_string))
        name = info_string[0: info_string.index(":")]
        sum_hours = []
        for el in hours:
            sum_hours.append(int(el))
        result_sum_hours = sum(sum_hours)
        result[name] = result_sum_hours
    print(result)
