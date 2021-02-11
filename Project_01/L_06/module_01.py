
import time

print("Урок 6. Пункт 1")


class TrafficLight(object):

    def __init__(self):
        self.__color = "off"

    def __str__(self):
        return "Светофор"

    def running(self):
        self.__color = "красный"
        print(self.__color)
        time.sleep(7)
        self.__color = "жёлтый"
        print(self.__color)
        time.sleep(2)
        self.__color = "зелёный"
        print(self.__color)
        time.sleep(5)
        self.__color = "off"


light = TrafficLight()
print(light)
light.running()
