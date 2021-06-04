from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while True:
            if i == 0:
                print(f'{TrafficLight.__color[i]}')
                sleep(7)
                i += 1
                continue
            elif i == 1:
                print(f'{TrafficLight.__color[i]}')
                sleep(2)
                i += 1
                continue
            elif i == 2:
                print(f'{TrafficLight.__color[i]}')
                sleep(9)
                i = 0
                continue


object = TrafficLight()
object.running()
