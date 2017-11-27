

class Rational:
    def __init__(self, x, y):
        if type(x) != int or type(y) != int or y == 0:
            raise TypeError("Only integres are allowed")
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

    def reduce_rational(self):
        if self.x % 2 == 0 and self.y % 2 == 0:
            while self.x % 2 == 0 and self.y % 2 == 0:
                self.x /= 2
                self.y /= 2
        return Rational(self.x, self.y)

    def __eq__(self, other):
        return self.x * other.y == self.y * other.x

    def __str__(self):
        return "<x={}, y={}>".format(
            self.x,
            self.y
        )

    def count_lcd(self, other):
        lcd = 1
        if self.y > other.y:
            for i in range(1, 100):
                if (self.y * i) % other.y == 0:
                    lcd = self.y * i
                    break
        elif self.y < other.y:
            for i in range(1, 100):
                if (other.y * i) % self.y == 0:
                    lcd = other.y * i
                    break
        else:
            lcd = self.y
        return lcd

    def __add__(self, other):
        lcd = 1
        if self.y > other.y:
            for i in range(1, 100):
                if (self.y * i) % int(other.y) == 0:
                    lcd = self.y * i
                    break
        elif self.y < other.y:
            for i in range(1, 100):
                if (other.y * i) % int(self.y) == 0:
                    lcd = other.y * i
                    break
        else:
            lcd = self.y
        return Rational(
            (int(lcd / self.y) * self.x) + (int(lcd / other.y) * other.x), lcd
        )


if __name__ == "__main__":
    print("Start Tests")
    a = Rational(2, 4)
    b = Rational(4, 5)

    assert Rational(2, 6) == Rational(1, 3)
    assert Rational(1, 3) == Rational(1, 3)
    assert Rational(4, 3) == Rational(8, 6)

    n = a + b
    assert n == Rational(26, 20)

    x = a * b
    assert x == Rational(8, 20)
    a *= b
    assert a == Rational(8, 20)



    print(a)
    print(b)
    print("End Tests")

    "fdfdf"

