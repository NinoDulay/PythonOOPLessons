#Inheritance
# Inheritance is isang proseso na ang isang child class gumagaya sa parent class

class Parent:
    def __init__(self, name, age, faveColor):
        self.name = name
        self.age = age
        self.faveColor = faveColor

    def introduce(self):
        print("My name is", self.name, "and I am", self.age, "years old")

# class Father:
#     pass

class Child(Parent):
    def __init__(self, name, age, faveColor, faveFood, money):
        # super() = Parent
        super().__init__(name, age, faveColor)
        self.faveFood = faveFood
        self.money = money

    def introduce(self):
        print("My name is", self.name, "and I am", self.age, "years old")
        print("My favorite color is", self.faveColor)

# class Child2(Parent):
#     pass

# class Child3(Parent):
#     pass

p = Parent("Nino", 25, "Green")
p.introduce()

print()

c = Child("Nino", 16, "Black", "Chicken", 500)
c.introduce()


# class Child(Parent):
#     pass


# Exercise
# Shape - Parent
# Shape Atrribute - Sides

# Circle - Child class of Shape
# Circle - sides, diameter

# Square - Child class of shape
# Square - sides, color

# Inheritance
class Shape:
    def __init__(self, sides):
        self.sides = sides

class Circle(Shape):
    def __init__(self, sides, diameter):
        super().__init__(sides)
        self.diameter = diameter

class Square(Shape):
    def __init__(self, sides, color):
        super().__init__(sides)
        self.color = color



