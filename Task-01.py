# Задача 1. Машина 3

class Toyota():

    def __init__(self, color='', price=0, max_speed=0, current_speed=0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def print_info(self):
        print(f'Цвет: {self.color}\n'
              f'Цена: {self.price}\n'
              f'Максимальная скорость: {self.max_speed}\n'
              f'Текущая скорость: {self.current_speed}')

    def set_current_speed(self, speed):
        self.current_speed = speed
        print(f'Скорость изменена. Текущее значение {self.current_speed}')


my_car = Toyota()
my_car.print_info()
my_car.set_current_speed(60)
my_car.print_info()

other_car = Toyota('black', 1000000, 200, 120)
other_car.print_info()
