
index = int
string_in_file = str
words_in_file = list
words_string_length = int

print("Урок 5. Пункт 2")

index = 0

with open("file_2.txt", "r", encoding="utf-8") as file_to_read:
    for string_in_file in file_to_read:
        words_in_file = string_in_file.split()
        words_string_length = len(words_in_file)
        print(f"В строке №{index} ({words_in_file}) количество слов: {words_string_length}")
        index = index + 1

print(f"Общее количество строк в файле: {index}")
