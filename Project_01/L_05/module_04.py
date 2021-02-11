
number_dict = dict
file_result = list

print("Урок 5. Пункт 4")

number_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_result = []

with open("file_4.txt", "r", encoding="utf-8") as file_to_read:
    for string_from_file in file_to_read:
        name_from_file = string_from_file[0: string_from_file.index(" ")]
        new_string_from_file = string_from_file.replace(name_from_file, number_dict.get(name_from_file))
        file_result.append(new_string_from_file)

with open("file_4_w.txt", "w", encoding="utf-8") as file_to_write:
    file_to_write.writelines(file_result)
