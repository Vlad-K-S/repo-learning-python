
number_of_cells_in_str = int

print("Урок 7. Пункт 3")


class OrganicCellGroup(object):

    def __init__(self, number_cells):
        self.number_cells = number_cells
        # Количество клеток в группе клеток

    def __add__(self, other):
        # сложение
        add_cells = self.number_cells + other.number_cells
        return add_cells

    def __sub__(self, other):
        # вычитание
        if (self.number_cells - other.number_cells) > 0:
            sub_cells = self.number_cells - other.number_cells
        else:
            sub_cells = "Первая группа клеток меньше второй. " \
                        "Вычитание даёт отрицательный результат."
        return sub_cells

    def __mul__(self, other):
        # умножение
        mul_cells = self.number_cells * other.number_cells
        return mul_cells

    def __truediv__(self, other):
        # деление
        truediv_cells = self.number_cells // other.number_cells
        return truediv_cells

    def make_order(self, number_of_cells_in_string):
        self.number_of_cells_in_string = number_of_cells_in_string
        number_of_cells_in_string_all = self.number_of_cells_in_string
        list_new = []
        ind = 0
        index = 0
        for ind in range(self.number_cells):
            list_new.append("*")
        for index in range(self.number_cells // self.number_of_cells_in_string):
            list_new.insert(number_of_cells_in_string_all, "\n")
            number_of_cells_in_string_all = self.number_of_cells_in_string + number_of_cells_in_string_all + 1
        result_in_order = "".join(list_new)
        return result_in_order


oc_1_numb = int(input("Введите количество клеток в первой группе: "))
oc_2_numb = int(input("Введите количество клеток во второй группе: "))
oc_1 = OrganicCellGroup(oc_1_numb)
oc_2 = OrganicCellGroup(oc_2_numb)
number_of_cells_in_str = int(input("Введите количество клеток в строке: "))
print(f"Сложение: {oc_1 + oc_2}")
print(f"Вычитание: {oc_1 - oc_2}")
print(f"Умножение: {oc_1 * oc_2}")
print(f"Деление: {oc_1 / oc_2}")
print(f"Первая группа клеток по рядам: \n{oc_1.make_order(number_of_cells_in_str)}")
print(f"Вторая группа клеток по рядам: \n{oc_2.make_order(number_of_cells_in_str)}")
