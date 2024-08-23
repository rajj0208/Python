class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if(value > 0):
            self._age = value
        else:
            raise ValueError("Age cannot be negative")


a = Person(25)

print(a.age)

try:
    a.age = -10
except ValueError as e:
    print(e)