class Mammal:
    def walk(self):
        print("Walking on four legs")

class Flying:
    def fly(self):
        print("Flying in the sky")

class Bat(Mammal, Flying):
    def hunt(self):
        print("Hunting insects")

# Create a Bat object
bat = Bat()

# Access methods from both parent classes
bat.walk()
bat.fly()   
bat.hunt()  

print(Bat.mro())