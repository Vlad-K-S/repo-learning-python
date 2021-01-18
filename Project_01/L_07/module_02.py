
print("Урок 7. Пункт 2")


class Clothes(object):

    def __init__(self, size_coat, size_suit):
        self.size_coat = size_coat
        self.size_suit = size_suit

    @property
    def sum_fabrics(self):
        sum_fabrics_all = self.size_coat / 6.5 + 0.5 + 2 * self.size_suit + 0.3
        return f"Расход ткани на пальто и костюм: {sum_fabrics_all} м2"


class Coat(Clothes):

    def __init__(self, size_coat):
        self.size_coat = size_coat

    @property
    def sum_fabrics(self):
        sum_fabrics_coat = self.size_coat / 6.5 + 0.5
        return f"Расход ткани на пальто: {sum_fabrics_coat} м2"


class Suit(Clothes):

    def __init__(self, size_suit):
        self.size_suit = size_suit

    @property
    def sum_fabrics(self):
        sum_fabrics_suit = self.size_suit * 2 + 0.3
        return f"Расход ткани на костюм: {sum_fabrics_suit} м2"


v_size = int(input("Введите размер для пальто: "))
h_size = int(input("Введите рост для костюма: "))
clothes_result = Clothes(v_size, h_size)
print(clothes_result.sum_fabrics)
coat_result = Coat(v_size)
print(coat_result.sum_fabrics)
suit_result = Suit(h_size)
print(suit_result.sum_fabrics)
