class Animal:
    def __init__(self):
        print(f'Cats talk: "{self.voice}"')
class Dog(Animal):
    def __init__(self, voice):
        self.voice = voice
        super().__init__()
class Cat(Animal):
    def __init__(self, voice):
        self.voice = voice
        super().__init__()

dog = Dog("Fuuuf")
cat = Cat("Meow")