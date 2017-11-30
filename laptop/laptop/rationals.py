

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

    def __reduce__(self):
        if self.x > self.y:
            i = 1
            while i:
                if self.x % self.y == 0:
                    return Rational(int(self.x / self.y), int(self.y / self.y))
                if self.x % 2 == 0 and self.y % 2 == 0:
                    self.x /= 2
                    self.y /= 2
                    continue
                if self.x % 3 == 0 and self.y % 3 == 0:
                    self.x /= 3
                    self.y /= 3
                    continue
                else:
                    return Rational(int(self.x), int(self.y))
        if self.y > self.x:
            i = 1
            while i:
                if self.y % self.x == 0:
                    return Rational(int(self.x / self.x), int(self.y / self.x))
                if self.x % 2 == 0 and self.y % 2 == 0:
                    self.x /= 2
                    self.y /= 2
                    continue
                if self.x % 3 == 0 and self.y % 3 == 0:
                    self.x /= 3
                    self.y /= 3
                    continue
                else:
                    return Rational(int(self.x), int(self.y))
        else:
            return Rational(1, 1)

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

    def __sub__(self, other):
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
            (int(lcd / self.y) * self.x) - (int(lcd / other.y) * other.x), lcd
        )

    def __truediv__(self, other):
        return Rational(
            self.x * other.y,
            self.y * other.x
        )


if __name__ == "__main__":
    print("Start Tests")
    a = Rational(2, 4)
    b = Rational(4, 5)
    c = Rational(2, 4)

    assert Rational(2, 6) == Rational(1, 3)
    assert Rational(1, 3) == Rational(1, 3)
    assert Rational(4, 3) == Rational(8, 6)

    n = a + b
    assert n == Rational(26, 20)

    m = a - b
    assert m == Rational(-6, 20)

    k = a / b
    assert k == Rational(10, 16)

    x = a * b
    assert x == Rational(8, 20)
    a *= b
    assert a == Rational(8, 20)

    assert c.__reduce__() == Rational(1, 2)

    print(a)
    print(b)
    print(n)
    print(m)
    print(k)
    print(c.__reduce__())
    print("End Tests")

