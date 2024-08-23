#A basic example of single inheritence
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print(f"The animal {self.name} make sound : SOUND")

class Dog(Animal):
    def make_sound(self):
        print("BARK!!!!")


a = Animal("DOG")
a.make_sound()

d = Dog("Dog")
d.make_sound()