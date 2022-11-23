

class Transport:
    def __str__(self):
        return 'Transport created'


class Bicycle(Transport):
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return f'Maximum bicycle speed: {self.max_speed}'


class Car(Transport):
    def __init__(self, horsepower, engine_volume):
        self.horsepower = horsepower
        self.engine_volume = engine_volume

    def upgrade(self, k):
        self.horsepower += k

    def __str__(self):
        return f'The car has {self.horsepower} h.p. and engine volume {self.engine_volume} l.'


class Colors(Transport):
    def __init__(self, transport, color):
        self.transport = transport
        self.color = color

    def __str__(self):
        return f'{self.transport} is {self.color}'