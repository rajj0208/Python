#super key world is used to call the methods of parent class

class Emp:
    def show(self):
        print("This is parent class")


class prog(Emp):
    def info(self):
        print("This is child class")
        super().show()



p = prog()
p.info()

prog.info(p) # this way you can understand that how object is passed while calling the methods
# therefor self has to be written as parameter in methods in class