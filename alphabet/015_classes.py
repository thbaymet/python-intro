class Dog:

    # Class object attribute
    species = 'mammal'

    def __init__(self, breed, name, has_spots):
        self.breed = breed
        self.name = name
        self.has_spots = has_spots

    def bark(self):
        print("WOOF !!!")


my_dog = Dog(breed='Lab', name='Dock', has_spots=True)
print("type(my_object): ", type(my_dog))
print("type(my_object): ", my_dog.breed)
my_dog.bark()


class Circle:

    pi = 3.14

    def __init__(self, radius=10):
        self.radius = radius
        self.area = Circle.pi * radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius


circle = Circle(5)
print("circle.area: ", circle.area)
print("circle.circumference: ", circle.circumference())


