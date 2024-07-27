class Animal:
    def speak():
        return"speaking..."
class Dog(Animal):
    def speak():
        return"dog is speaking..."
class Puppy(Dog):
    def speak():
        return"puppy is speaking..."
obj=Dog
print(obj.speak())    
      

