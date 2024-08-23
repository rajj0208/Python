from typing import Any


class magic:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ("I am a magic/dunder function")
    
    def __call__(self, *args):
        sum = 0
        for item in args:
            sum += item
        print("Object can be made callable using this dunder fucntion", sum)


m = magic("Black magic")

print(str(m))
m(1, 2, 3, 4, 5 , 6)