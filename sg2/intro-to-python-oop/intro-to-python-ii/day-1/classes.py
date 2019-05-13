# different than self.leg_count in Animal class
leg_count = 2


class Animal:
    def __init__(self, leg_count):
        self.leg_count = leg_count
        self.name = "Animal"

    def get_leg_count(self):
        print(self.leg_count)

    def set_leg_count(self, leg_count):
        self.leg_count = leg_count


a = Animal(4)

a.get_leg_count()
# print(leg_count)
a.set_leg_count(3)
a.get_leg_count()


class Motor:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Car:
    def __init__(self):
        self.motor = Motor(40)


car = Car()
print(car.motor.horsepower)
