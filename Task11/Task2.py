class Dog:
    def __init__(self, dogs_age):
        self.age_factor = 7
        self.__human(dogs_age)
    def __human(self, dogs_age):
        self.dogs_age = dogs_age*self.age_factor
        return print(self.dogs_age)

m = Dog(10)
