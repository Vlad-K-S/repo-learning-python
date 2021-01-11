
result_sum = float
switch = bool

print("Урок 3. Пункт 5")
print("Суммирование введённых чисел. Цикл прервётся, если ввести символ &")
print("Введите, пожалуйста, строку чисел, разделённых пробелами: ")

result_sum = 0
switch = False


def func_string_sum(result_string_sum, switch_in):
    string_with_numbers = input("")
    spec_symbol_place = string_with_numbers.find("&")
    if spec_symbol_place >= 0:
        string_with_numbers_slace = string_with_numbers[:(spec_symbol_place - 1)]
        switch_in = True
    else:
        string_with_numbers_slace = string_with_numbers
    list_with_numbers = []
    list_with_numbers = string_with_numbers_slace.split(" ")
    for item_list in list_with_numbers:
        if item_list.isdigit():
            item_list = float (item_list)
            result_string_sum = result_string_sum + item_list
    print(result_string_sum)
    return result_string_sum, switch_in


while not switch:
    result_sum, switch = func_string_sum(result_sum, switch)
    print(f"Сумма чисел: {result_sum}")
else:
    print("Суммирование закончено.")
