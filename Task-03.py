# Задача 3. Весёлая ферма

class Potato:
    stage = 0
    stages = ('ничего нет', 'росток', 'зеленая', 'зрелая')

    def __init__(self, number):
        self.number = number

    def grow(self):
        self.print_grow()
        if self.stage < len(self.stages) - 1:
            self.stage += 1

    def print_grow(self):
        print(f'Куст картошки под номером :{self.number} статус: {self.stages[self.stage]}')

    def status_potato(self):
        if self.stages[self.stage] == 'зрелая':
            return True
        return False


class Garden:

    def __init__(self, numbers):
        self.numbers = [Potato(i) for i in range(1, numbers + 1)]

    def all_grow(self):
        print('Картофель поспевает...\n')
        for i in self.numbers:
            i.grow()

    def ready_to_eat(self):
        if all([Potato.status_potato(i) for i in self.numbers]):
            print('\nКартошку можно собирать.')
        else:
            print('\nПока собирать картошку нельзя.')


my_patch = Garden(5)
for _ in range(4):
    my_patch.all_grow()
    my_patch.ready_to_eat()
