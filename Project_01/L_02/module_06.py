
question = str
index = int
result = list
spec = list
spe = str
res_dict = dict
item = dict
param = int

index = 1
result = []
spec = ["название", "цена", "количество", "единица измерения"]

print("Урок 2. Пункт 6")

while True:
    question = input("Добавить новый товар? да/нет")
    if question.lower() == "нет":
        break
    item = {}

    for spe in spec:
        user_data = input(f"Введите {spe} ")
# Просим ввести значения товаров
        if user_data.isdigit():
            item[spe] = int(user_data)
        else:
            item[spe] = user_data
    result.append(tuple([index, item]))
    index = index + 1

res_dict = {}

for item in spec:
    for param in result:
        if res_dict.get(item):
            res_dict[item].append(param[1].get(item))
        else:
            res_dict[item] = [param[1].get(item)]

print(res_dict)
