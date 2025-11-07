"""
Problem-1: Animal Hierarchy
Goal: Class Animal → method speak().
Child classes: Dog, Cat, Cow.
Each prints a different sound.
Focus: Basic single inheritance.
"""
print("-----------------------------------Problem-1 solution----------------------")

class Animal:
    def speak(self):
        print("This animal makes a sound.")
class Dog(Animal):
    def speak(self):
        print(" Dog says: Woof! Woof!")
class Cat(Animal):
    def speak(self):
        print("Cat says: Meow! Meow!")
class Cow(Animal):
    def speak(self):
        print(" Cow says: Moo! Moo!")
# Polymorphism — same method, different behavior
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.speak()


"""
Problem-2: Multi-Level Inheritance
Goal: Create Person → Employee → Manager.
Each has its own method.
Hint: Use super() to call parent constructor.
Focus: Multi-level inheritance & constructor chaining.
"""
print("-----------------------------------Problem-2 solution----------------------")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_person(self):
        print(f'name: {self.name} , Age: {self.age}')
class Employee(Person):
    def __init__(self, name, age,emp_id):
        super().__init__(name,age)
        self.emp_id=emp_id
    def show_employee(self):
        print(f'Employee ID: {self.emp_id}')
class Manager(Employee):
    def __init__(self, name, age, emp_id,department):
        super().__init__(name, age, emp_id)
        self.department=department
    def show_manager(self):
        print(f'Manager of {self.department} department')

m1=Manager("Vishal Pal",24,"EMP01","IT")
m1.show_person()
m1.show_employee()
m1.show_manager()


"""
Problem-3: Multiple Inheritance
Goal: Create classes Flyable, Swimmable, Duck(Flyable, Swimmable).
Hint: Use methods fly() and swim().
Focus: Multiple inheritance and MRO (Method Resolution Order).
"""
print("-----------------------------------Problem-3 solution----------------------")

class Flyable:
    def fly(self):
        print("This animal can fly in the sky!")
class Swimmable:
    def swim(self):
        print("This animal can swim in water!")
class Duck(Flyable, Swimmable):
    def sound(self):
        print("Duck says: Quack! Quack!")
# Create Duck object (inherits from both)
d = Duck()
d.fly()
d.swim()
d.sound()
print("MRO:", [cls.__name__ for cls in Duck.__mro__])


