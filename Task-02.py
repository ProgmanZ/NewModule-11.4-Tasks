# Задача 2. Координаты точки

class Point:

    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1

    def print_info(self):
        print(f'x = {self.x} y = {self.y}')
        print(f'Создано точек {self.count}')


point_a = Point(1, 2)
point_a.print_info()

point_b = Point(10, 5)
point_b.print_info()

point_c = Point(4, 6)
point_c.print_info()
