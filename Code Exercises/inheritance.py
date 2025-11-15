class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name} is {self.age} years old.")

    def speak(self):
        print("I don't know what to say.")

class Dog(Pet):
    def speak(self):
        print("Woof")

class Cat(Pet):
    def speak(self):
        print("Meow")


p = Pet("Buddy", 4)
p.show()

c = Cat("Whiskers", 3)
c.show()
c.speak()

d = Dog("Rex", 5)
d.show()
d.speak()

# Example of a ternary conditional operator in Python
age = 12
message = "Eligible" if age >=18 else "Not Eligible"
print(message)