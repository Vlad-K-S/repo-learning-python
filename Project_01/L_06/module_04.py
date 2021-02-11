
print("Урок 6. Пункт 4")


class Car(object):

    def __init__(self, speed=0, color="", name="", is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.car_property = [self.speed, self.color, self.name, self.is_police]

    def go(self):
        print("Автомобиль поехал")

    def stop(self):
        print("Автомобиль остановился")

    def turn(self, direction):
        print(f"Автомобиль повернул {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"Превышение скорости")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"Превышение скорости")


class PoliceCar(Car):
    pass


car_all = Car(40, "white", "Ford", False)
car_town_slow = TownCar(30, "blue", "Toyota", False)
car_town_fast = TownCar(70, "red", "Toyota", False)
car_sport = SportCar(80, "red", "Toyota")
car_work_slow = WorkCar(20, "green", "Nissan", False)
car_work_fast = WorkCar(50, "green", "Nissan", False)
car_police = PoliceCar(50, "black", "Ford", True)

print(car_all.car_property)
car_all.show_speed()
print(car_town_slow.car_property)
car_town_slow.show_speed()
print(car_town_fast.car_property)
car_town_fast.show_speed()
print(car_sport.car_property)
car_sport.show_speed()
print(car_work_slow.car_property)
car_work_slow.show_speed()
print(car_work_fast.car_property)
car_work_fast.show_speed()
print(car_police.car_property)
car_police.show_speed()

car_sport.go()
car_sport.turn("налево")
car_sport.turn("направо")
car_sport.stop()
