class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self, hours):
        print(f"{self.name} is sleeping for {hours} hours.")

    def make_sound(self):
        print(f"{self.name} is making sound.")

class Cow(Animal):
    def __init__(self, name, age, milk_capacity):
        super().__init__(name, age)
        self.milk_capacity = milk_capacity

    def make_sound(self):
        print(f"{self.name} says Moo!")

    def milk(self):
        print(f"{self.name} produces {self.milk_capacity} liters of milk")

class Chicken(Animal):
    def __init__(self, name, age, egg_count):
        super().__init__(name, age)
        self.egg_count = egg_count

    def make_sound(self):
        print(f"{self.name} says Cluck!")

    def egg(self):
        print(f"{self.name} lays {self.egg_count} eggs.")

class Sheep(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def make_sound(self):
        print(f"{self.name} says Maa-a-a-a!")

    def fighting(self, other):
        if not isinstance(other, Sheep) or other == '':
            raise ValueError("Opponent should be a sheep")
        elif self.gender != 'male' or other.gender != 'male':
            raise ValueError("Both sheeps should be male")
        print(f"{self.name} is fighting with {other.name} in the field.")


cow1 = Cow('Bessy', 4, 20)
chicken1 = Chicken('Tikki', 1, 2)
sheep1 = Sheep('Bull', 2, 'male')
sheep2 = Sheep('Budd', 2, 'male')
sheep3 = Sheep('Chica', 1, 'female')

sheep1.eat('grass')
sheep1.fighting(sheep2)





    



