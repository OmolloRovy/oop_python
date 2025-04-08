# Animal class with a move method
class Animal:
    def move(self):
        print("The animal moves!")

# Dog class inherits from Animal
class Dog(Animal):
    def move(self):
        print("Running ")

# Bird class inherits from Animal
class Bird(Animal):
    def move(self):
        print("Flying ")

# Vehicle class with a move method
class Vehicle:
    def move(self):
        print("The vehicle is moving!")

# Car class inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving ")

# Plane class inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ")

# Creating instances of each class and calling their move method
def demonstrate_move():
    dog = Dog()
    bird = Bird()
    car = Car()
    plane = Plane()

    dog.move()
    bird.move()
    car.move()
    plane.move()

# Run the demonstration
demonstrate_move()
