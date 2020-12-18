
string_with_words = str
list_with_words = list
list_with_words_new = list
word_in = str

print("Урок 3. Пункт 6")

word_in = input("Введите, пожалуйста, слово строчными буквами: ")


def int_func(word_low):
    word_up = word_low.capitalize()
    return word_up

print(int_func(word_in))

list_with_words = []
list_with_words_new = []

string_with_words = input("Введите, пожалуйста, строку слов строчными буквами, разделённых пробелами: ")
list_with_words = string_with_words.split(" ")

for item in list_with_words:
    list_with_words_new.append(int_func(item))

print(' '.join(list_with_words_new))
