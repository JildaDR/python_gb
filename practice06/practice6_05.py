class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки для ручки.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки для маркера.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки для типа "{self.title}".')


pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()
