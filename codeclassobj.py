class person:
    name = "Raj Jaiswal"
    age = 24
    occupation = "AI Engineer"
    def info(self):
        print(f"The name is {self.name} and He is {self.occupation}")

a = person()
print(a.name, a.age, a.occupation)

a.occupation = "Software Developer"

print(a.occupation)
a.info()
