"""
Problem-1: Animal Sounds
Goal: Classes Dog, Cat, Bird with same method make_sound().
Loop through them and call make_sound().
Focus: Method overriding.
"""
print("-----------------------Problem-1 Solution--------------------") 
class  Animal:
    def make_sound(self):
        print("This is makes a sound")
class Dog(Animal):
    def make_sound(self):
            print("Dog say: woof! woof1")
class Cat(Animal):
     def make_sound(self):
         print("Cat says: meow! meow!")
class Bird(Animal):
     def make_sound(self):
        print(f'Bird says: chii! chii!' )
dog=Dog()
dog.make_sound()
cat=Cat()
cat.make_sound()
bird=Bird()
bird.make_sound()


"""
Problem-2: Len Function
Goal: Class Playlist → store songs in a list.
Implement __len__() to return number of songs.
Focus: Built-in function polymorphism.
"""
print("-----------------------Problem-2 Solution--------------------")
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

my_playlist = Playlist(["Song1", "Song2", "Song3","Song4"])
print(len(my_playlist)) 

"""
Problem-3: Method Overriding with Super()
Goal: Employee → parent class with work().
Manager(Employee) overrides work() but calls parent using super().
Focus: Use of overridden method and parent call.
"""
print("-----------------------Problem-3 Solution--------------------")
class Employee:
    def work(self):
        print("Employee is working 9 to 5.")
class Manager(Employee):
    def work(self):
        super().work() 
        print("Manager is also attending meetings and managing team.")

m = Manager()
m.work()

"""
Problem-4: Shape Drawing
Goal: Classes Circle, Square, Triangle → all have draw() method.
Loop through and call draw() to print shape name.
Focus: Dynamic method binding.
"""
print("-----------------------Problem-4 Solution--------------------")
class Shape:
    def draw(self):
        print("Drawing a shape...")
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")
class Square(Shape):
    def draw(self):
        print("Drawing a Square")
class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")
shapes = [Circle(), Square(), Triangle()]
for shape in shapes:
    shape.draw()

