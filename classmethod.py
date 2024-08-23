# class method is associated with class rather than object 

class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def show(self):
        print(f"The name of employee is {self.name} and he is {self.age} years old and his salary is {self.pay}")
        
    @classmethod
    def obj_from_string(cls, emp_str):
        l = emp_str.split('-')
        return cls(l[0], int(l[1]), int(l[2]))
    
    

    
    
e1 = Employee("Raj", 24, 100000)
e2 = Employee.obj_from_string("Riya-27-100000")

e1.show()
e2.show()
