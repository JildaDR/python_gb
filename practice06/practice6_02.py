class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculator(self):
        while True:
            try:
                a = int(input('необходимое количество асфальта (в кг) на 1м кв толщиной в 1 см: '))
            except (TypeError, ValueError):
                print('Введите положительное число')
                continue
            if a <= 0:
                print('Введите положительное число')
                continue
            break
        while True:
            try:
                b = int(input('Необходимая толщина слоя асфальта в см: '))
            except (TypeError, ValueError):
                print('Введите положительное число')
                continue
            if b <= 0:
                print('Введите положительное число')
                continue
            break
        result = self._length * self._width * a * b / 1000
        print(f'на покрытие дороги шириной в {self._width}м, длиной в {self._length}м, '
              f'слоем асфальта толщиной в {b}см необходимо {result} тонн асфальта')


road = Road(5000, 25)
road.calculator()
