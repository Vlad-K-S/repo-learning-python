
print("Урок 6. Пункт 2")


class Road(object):

    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def asphalt_mass(self):
        result_asphalt_mass = self.length * self.width * 10 * 4
        # На 1 кв.метр толщиной 1 см
        # Масса асфальта 10 кг
        # Толщина дорожного полотна 4 см
        return result_asphalt_mass


road_length = int(input("Введите длину дороги в сантиметрах:"))
road_width = int(input("Введите ширину дороги в сантиметрах:"))
road_new = Road(road_length, road_width)
print(f"Масса асфальта для покрытия дорожного полотна: {road_new.asphalt_mass()} кг")
