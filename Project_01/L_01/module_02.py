
second_inp = int
second_out = int
minute_out = int
hour_out = int

print("Урок 1. Пункт 2")

second_inp = int(input("Введите, пожалуйста, время в секундах: "))
hour_out = second_inp // 3600
minute_out = (second_inp - (hour_out * 3600)) // 60
second_out = second_inp % 60
print(f"Запишем это так: {hour_out}:{minute_out}:{second_out}")