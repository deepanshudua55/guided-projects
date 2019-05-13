class Animal:
    # constructor
    # two arguments - leg count and speed
    # leg count should default to 2
    # speed should default to 5
    def __init__(self, legs=2, speed=5):
        # set the class properties to equal the arguments
        self.legs = legs
        self.speed = speed

    def sound(self):
        return "Generic sound"

# Animal -> Quadruped


class Quadruped(Animal):
    def __init__(self):
        # first argument is 4, setting the leg count
        # speed stays the same
        super().__init__(4)

# Animal -> Quadruped -> Cat


class Cat(Quadruped):
    def sound(self):
        return "Meow"

# Animal -> Quadruped -> Dog


class Dog(Quadruped):
    def sound(self):
        return "Bark"

# Animal -> Quadruped -> Cat -> Lion


class Lion(Cat):
    def sound(self):
        return "Roar!"

# Animal -> Human


class Human(Animal):
    def sound(self):
        return "Argh!"


animals = [Animal(),
           Cat(),
           Dog(),
           Lion(),
           Human()]

sounds = [animal.sound() for animal in animals]

print(sounds)
