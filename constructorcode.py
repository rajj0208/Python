class detail:
    # def __init__(self):
    #     print("I am a default constructor")
    def __init__(self, names, occs):
        self.name = names
        self.occ = occs
        print("I am a parameterized constructer")


    def info(self):
        print(f"{self.name} is a {self.occ}")


a = detail("Raj jaiswal", "AI engineer")
a.info()
