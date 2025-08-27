class Vehicle:
    def move(self):
        pass   # To be overridden by each child class

class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing ⛵")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each prints its own unique version
