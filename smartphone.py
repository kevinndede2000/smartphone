# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

    def __str__(self):
        return f"Device: {self.brand} {self.model}"


# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
        self.__battery = 100  # private attribute (encapsulation)

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f" {self.brand} {self.model} is charging... Battery: {self.__battery}%"

    def use(self, hours):
        self.__battery = max(0, self.__battery - hours * 10)
        return f" {self.brand} {self.model} used for {hours} hrs → Battery: {self.__battery}%"

    def get_battery(self):
        return f" {self.brand} {self.model} battery at {self.__battery}%"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.os}, {self.storage})"


# --------- TESTING PART 1 ----------
print("=== Part 1: Smartphone Class Demo ===\n")
phone1 = Smartphone("Samsung", "Galaxy S24", "Android", "256GB")
phone2 = Smartphone("Apple", "iPhone 15", "iOS", "512GB")

# Dynamic simulation
for phone in [phone1, phone2]:
    print(f" Testing: {phone}")
    print(phone.info())
    print(phone.use(2))
    print(phone.use(1))
    print(phone.charge(15))
    print(phone.get_battery())
    print("-" * 40)


# ===========================
# PART 2: Polymorphism Demo
# ===========================

class Animal:
    def speak(self):
        return "This animal makes a sound."

class Dog(Animal):
    def speak(self):
        return " Dog says: Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return " Cat says: Meooow!"

class Cow(Animal):
    def speak(self):
        return " Cow says: Moooo!"

class Parrot(Animal):
    def speak(self):
        return " Parrot says: Hello there!"
class kochieng(Animal):
    def speak(self):
        return " kochieng says: good morning my neighbors!"


# --------- TESTING PART 2 ----------
print("\n===  Part 2: Polymorphism Demo ===\n")
animals = [Dog(), Cat(), Cow(), Parrot(),kochieng()]

for animal in animals:
    print(animal.speak())
