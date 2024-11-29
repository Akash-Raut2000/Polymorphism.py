class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# Using polymorphism
def make_sound(animal):
    print(animal.sound())

# Real-life usage
animals = [Dog(), Cat()]
for animal in animals:
    make_sound(animal)
