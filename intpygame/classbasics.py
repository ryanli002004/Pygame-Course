class Dog():

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age 
    
    def eat(self):
        if self.gender == "male":
            print("Here "+ self.name + " Good boy! eat up.")
        else:
            print("Here "+ self.name+ " Good girl! Eat up.")

    def bark(self, isloud):
        if isloud:
            print("WOOF WOOF")
        else: 
            print("woof")

    def computeage(self):
        dogyears = self.age * 7
        print(self.name + " is " + str(dogyears) +" dog years old")

mydog = Dog("spot","male",10)
mydog2 = Dog("katie", "female", 12)

print(mydog.name)
print(mydog2.gender)
mydog.name = "roger"
print(mydog.name)
print()
mydog.eat()
mydog2.eat()
print()
mydog.bark(True)
mydog2.bark(False)
print()
mydog.computeage()
mydog2.computeage()