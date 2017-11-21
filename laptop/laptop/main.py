from animals import Dog, Cat

cat_1 = Cat("black", "m", 0, name="Snow")
cat_2 = Cat("white", "f", 7, name="Godzilla")

print(cat_1 + cat_2)
print(cat_1.__add__(cat_2))
print(Cat.__add__(cat_1, cat_2))
print(cat_1 - cat_2)
print(cat_1 < cat_2)
print(cat_1 > cat_2)
print(cat_1 == cat_2)
print(bool(cat_1))
print(cat_1(2, 3))

d = {
    cat_1: "Meow"
}
print(d[cat_1])
