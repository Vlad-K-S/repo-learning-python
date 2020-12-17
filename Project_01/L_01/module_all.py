
t01 = int
t02 = float
t03 = float
st01 = str

second_inp = int
second_out = int
minute_out = int
hour_out = int

n = str
nn = str
nnn = str
nnnnnn = int

w = int
f = int
g = int
m = int

proceeds = float
costs = float
profit = float
roi = float
staff = int
proceeds_staff = float

a = float
b = float
dayx = int

print('Hello earthling.')
print('So we begin.')

print("Урок 1. Пункт 1")

t01 = int(input("Введите, пожалуйста, целое число: "))
t02 = float(input("Введите, пожалуйста, число: "))
st01 = input("Введите, пожалуйста, текст: ")
t03 = t01 + t02
print("И, если это сложить, получится:", st01, t03)

print("Урок 1. Пункт 2")

second_inp = int(input("Введите, пожалуйста, время в секундах: "))
hour_out = second_inp // 3600
minute_out = (second_inp - (hour_out * 3600)) // 60
second_out = second_inp % 60
print(f"Запишем это так: {hour_out}:{minute_out}:{second_out}")

print("Урок 1. Пункт 3")
n = input("Введите, пожалуйста, целое положительное число: ")
nn = n + n
nnn = n + n + n
nnnnnn = int(n) + int(nn) + int(nnn)
print(f"Тогда: {n} + {nn} + {nnn} = {nnnnnn}")

print("Урок 1. Пункт 4")

w = int(input("Введите, пожалуйста, целое положительное число: "))
g = w
m = w % 10

if g > 0:
    while g > 0:
        f = g % 10
        g = g // 10
        if f > m:
            m = f
    else:
        print(f"Самая большая цифра в числе: {m}")
else:
    print("Введено отрицательное число или ноль. Попробуйте ещё раз.")

print("Урок 1. Пункт 5")

proceeds = float(input("Введите, пожалуйста, выручку фирмы: "))
costs = float(input("Введите, пожалуйста, издержки фирмы: "))

if proceeds > costs:
    profit = proceeds - costs
    print(f"Фирма работает с прибылью {profit}")
    roi = profit / proceeds
    print(f"Соотношение прибыли и выручки {roi}")
    staff = int(input("Сообщите, пожалуйста, количество сотрудников фирмы: "))
    proceeds_staff = profit / staff
    print(f"Прибыль фирмы в рассчёте на одного сотрудника {proceeds_staff}")
else:
    print("Фирма работает с убытком")

print("Урок 1. Пункт 6")

print("Спортсмен занимается ежедневными пробежками.")
a = float(input("Пожалуйста, сообщите количество километров в первый день: "))
b = float(input("Пожалуйста, сообщите количество километров в день, который требуется найти: "))
dayx = 1

if a > b:
    print("Значения некорректные. Попробуйте ещё раз.")
elif a == b:
    print("День 1. Оба значения совпадают.")
else:
    while a < b:
        a = a * 0.1 + a
        dayx = dayx + 1
    else:
        print(f"Спортсмен достигает указанного результата (не менее {b} км) в день номер {dayx}")



