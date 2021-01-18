
text_from_file = []
text_input = str

print("Урок 5. Пункт 1")

with open("file_1.txt", "w", encoding="utf-8") as file_to_write:
    while True:
        text_input = input("Введите данные для внесения в файл: ")
        if text_input == "":
            break
        text_from_file.append(text_input)
        file_to_write.writelines(f"{text_input}\n")
