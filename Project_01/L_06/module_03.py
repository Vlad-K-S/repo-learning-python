
print("Урок 6. Пункт 3")


class Worker(object):

    def __init__(self, name="", surname="", position="", income={"Оклад": 0, "Премия": 0}):
        self.name = name
        self.surname = surname
        self.position = position
        self.surname = surname
        self.__income = income


class Position(Worker):

    @property
    def get_full_name(self):
        full_name = f"{self.surname} {self.name}"
        return full_name

    @property
    def get_total_income(self):
        total_income = self._Worker__income["Оклад"] + self._Worker__income["Премия"]
        return total_income


office_worker = Position("Виталий", "Иванов", "дизайнер", {"Оклад": 20000, "Премия": 10000})
print(office_worker.get_full_name)
print(office_worker.get_total_income)
