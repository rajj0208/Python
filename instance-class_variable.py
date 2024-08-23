class Employee:
    countEmp = 0 #class variale
    company = "Google"
    def __init__(self,name, id):
        self.name = name # instance varibale
        self.id = id
        Employee.countEmp += 1
    def showDetail(self):
        print(f"The name of employee {self.id} is {self.name} and he works in {self.company} where number of employees are {Employee.countEmp}")



e1 = Employee("Raj", 101)
e2 = Employee("Rahul", 102)
e3 = Employee("Rohan", 103)
e4 = Employee("Raja", 104)
#e1.showDetail() 
Employee.showDetail(e1) # with this example we can understand that object is passed to the function 
# which is taken as self argument in the class mehtod
e2.showDetail()
e3.showDetail()
e4.showDetail()

# Note: class variable can also be used for instance variable if it is present
# for example 
e1.company = "Apple" #Now the method will first check for instace variable
e1.showDetail()


