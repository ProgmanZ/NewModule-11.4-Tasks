# Задача 2. Координаты точки

class Point:
    count = 0
    points = list()

    def __init__(self, x, y):
        Point.count += 1
        self.x = x
        self.y = y

        self.points.append((self.x, self.y))

    def print_info(self):
        print(f'Текущие координаты: x:{self.x}, y:{self.y}.')
        print(f'Количество созданных точек: {self.count}.')
        print(f'Созданные точки:{self.points}')


my_points = Point(4, 6)
my_points.print_info()
other_point = Point(8, 7)
other_point.print_info()
