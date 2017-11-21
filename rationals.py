class Rational:
    def __init__(self, x, y):
        if type(x) != int or type(y) != int or y == 0:
            raise TypeError("Only intgeres are allowed")
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Rational(
            self.x * other.x,
            self.y * other.y
        )

    # TODO check it
    # do we really need methods with __i*__?
    # def __imul__(self, other):
    #     return self.__mul__(other)

    # def reduce_rational(self):
    #     return Rational()

    def __eq__(self, other):
        return self.x * other.y == self.y * other.x

    def __str__(self):
        return "<x={}, y={}>".format(
            self.x,
            self.y
        )


if __name__ == "__main__":
    print("Start Tests")
    a = Rational(2, 4)
    b = Rational(4, 5)

    assert Rational(2, 6) == Rational(1, 3)
    assert Rational(1, 3) == Rational(1, 3)
    assert Rational(4, 3) == Rational(8, 6)

    x = a * b
    assert x == Rational(8, 20)
    a *= b
    assert a == Rational(8, 20)

    print(a)
    print(b)
    print("End Tests")
