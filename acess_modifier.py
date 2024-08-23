#python donnot have public, private or protected attributes, but some methods can be used for convention


class Person:
    def __init__(self, name):
        self.__name = name

p = Person("Raj Jaiswal")

#python uses Name Mangling when we use __
print(p.__name)

#we can still acess it using

print(p._Person__name)