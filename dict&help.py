# dir() and __dict__ and help() helps us to understand the methods and attributes of class


# x = [1, 2, 3 ,4]
# print(dir(x))
# print(x.__dir__)
# print(help(x))

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"My name is {self.name}")


x = Person("raj", "24")
print(help(x))
