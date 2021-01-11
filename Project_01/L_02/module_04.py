
string_with_words = str
list_with_words = list
number = int
element = str

print("Урок 2. Пункт 4")

string_with_words = input("Введите, пожалуйста, нескольких слов, разделённых пробелами:")
list_with_words = string_with_words.split(" ")

for number, element in enumerate(list_with_words, 1):
    print(number, element[:10])
