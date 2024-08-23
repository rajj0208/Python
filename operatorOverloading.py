class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self, v):
        return Vector(self.i + v.i, self.j + v.j, self.k + v.k)

    

v1 = Vector(3, 6, 7)
print(v1)
v2 = Vector(6, 2, 5)
print(v2)

# now we want to do v1 + v2 but it wil show error show we have to overload the '+' operator using __add__

print(v1 + v2)