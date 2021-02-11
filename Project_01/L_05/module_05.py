

print("Урок 5. Пункт 5")

sum_numbers = 0

with open("file_5.txt", "w", encoding="utf-8") as file_to_write:
    string_numbers = input("Введите числа для сложения через пробел:")
    file_to_write.writelines(string_numbers)
    list_numbers = string_numbers.split(" ")
    for number_str in list_numbers:
        number_int = int(number_str)
        sum_numbers = sum_numbers + number_int
    print(f"Результат сложения: {sum_numbers}")
