class Employee:
    def __init__(self,name ,id):
        self.name = name
        self.id = id
    def info(self):
        print(f"The name of employee {self.id} is {self.name}")


class Programmer(Employee):
    def __init__(self, name, id, position, lang):
        super().__init__(name, id)
        self.position = position
        self.lang = lang
    def showInfo(self):
        print(f"The employee {self.name} is {self.lang} {self.position}")


e = Employee("Raj", 100)
e.info()
p = Programmer("Rahul", 101, "Software Developer", "c++")
p.info()
p.showInfo()