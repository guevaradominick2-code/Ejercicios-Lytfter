class Pet():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Makes a sound"
    
class Dog(Pet):
    def speak(self):
        return f"{self.name} says Woof Woof!"

class Cat(Pet):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Bamba")
print(dog.speak())

cat = Cat("Chimuelo")
print(cat.speak())
