# static method are associated with the class and can be used wihtout creating any instance/object

class Math:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def addition(a, b):
        return a + b
    


print(Math.addition(10 , 8))

n1 = Math(15)

print(n1.addition(15, 2))