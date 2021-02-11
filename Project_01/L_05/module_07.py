
import json

print("Урок 5. Пункт 7")

dict_profit = {}
dict_average_profit = {}
list_result_py = []
profit_sum = 0
n = 0

with open("file_7.txt", "r", encoding="utf-8") as file_to_read:
    for info_string in file_to_read:
        info_list = info_string.split(" ")
        company_profit = int(info_list[2]) - int(info_list[3])
        dict_profit[info_list[0]] = company_profit
        if company_profit > 0:
            profit_sum = profit_sum + company_profit
            n = n + 1
    dict_average_profit = {"average_profit": profit_sum/n}
list_result_py = [dict_profit, dict_average_profit]

print(list_result_py)

with open("file_7_j.json", "w") as file_to_write:
    json.dump(list_result_py, file_to_write)
