from base import Animal

print("Start Tests")
animal_test = Animal("black", 'M', 2)
assert animal_test.__class__.__name__ == "Animal"
print("End Tests")
