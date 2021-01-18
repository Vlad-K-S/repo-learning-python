
print("Урок 6. Пункт 5")


class Stationery(object):

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой.")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандашом.")


class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером.")


drawing = Stationery("Канцтовары")
drawing_pen = Pen("Ручка")
drawing_pensil = Pencil("Карандаш")
drawing_handle = Handle("Маркер")
print(drawing, drawing_pen, drawing_pensil, drawing_handle)
drawing.draw()
drawing_pen.draw()
drawing_pensil.draw()
drawing_handle.draw()
