from animals.base import Animal

class Cat(Animal):
    def voice(self):
        return "Meow meow"

    def __add__(self, other):
        if isinstance(other, Animal):
            return self.age + other.age
        raise TypeError("unsupported type: {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Animal):
            return self.age - other.age
        raise TypeError("unsupported type: {}".format(type(other)))

    def __gt__(self, other):
        if isinstance(other, Animal):
            return self.age > other.age
        raise TypeError("unsupported type: {}".format(type(other)))

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.age == other.age
        raise TypeError("unsupported type: {}".format(type(other)))

    def __bool__(self):
        return bool(self.age)

    def __hash__(self):
        return hash(self.name)

    def __call__(self, a, b):
        return self.age + a + b
