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

class Beagle(Dog):
    
    def __init__(self, name, gender, age, isgunshy):
        super().__init__(name,gender,age)
        self.isgunshy = isgunshy

    def hunt(self):
        if not self.isgunshy:
            self.bark(True)
            print(self.name + "is a good hunter")
        else: 
            print(self.name + "is not a good hunting dog  ")

    def bark(sefl,isloud):
        if isloud:
            print("HOWLLLL")
        else:
            print("howl")

dog1 = Beagle("kady", "female", 10, False)
dog1.eat() 
dog1.bark(False)
dog1.computeage()
dog1.hunt()