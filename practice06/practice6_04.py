class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        print(f'{self.name} is going')

    def stop(self):
        print(f'{self.name} is stopped')

    def turn(self):
        print(f'{self.name} is turned to the {self.direction}')

    def show_speed(self):
        print(f'{self.name} is going with speed {self.speed}')

    def result(self):
        while True:
            if self.speed > 0:
                self.go()
                self.show_speed()
                if self.direction != None:
                    self.turn()
                break
            else:
                self.stop()
                break


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} exceeded speed 60km/h and is going with speed {self.speed}km/h')
        else:
            print(f'{self.name} is going with speed {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} exceeded speed 40km/h and is going with speed {self.speed}km/h')
        else:
            print(f'{self.name} is going with speed {self.speed}')


class PoliceCar(Car):
    pass


Mercedes_Benz = TownCar(0, 'grey', 'Mercedes', False, None)
Mercedes_Benz.result()
Toyota = WorkCar(60, 'blue', 'Toyota', False, 'left')
Toyota.result()
Volkswagen = PoliceCar(80, 'white', 'Volkswagen', True, None)
Volkswagen.result()
BMW = TownCar(40, 'red', 'BMW', False, 'right')
BMW.result()
Porsche = SportCar(0, 'red', 'Porsche', False, None)
Porsche.result()
Honda = SportCar(120, 'black', 'Honda', False, 'left')
Honda.result()
Ford = WorkCar(30, 'green', 'Ford', False, None)
Ford.result()
Nissan = TownCar(50, 'yellow', 'Nissan', False, None)
Nissan.result()
