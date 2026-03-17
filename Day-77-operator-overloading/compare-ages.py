class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} age is {self.age}"

    def __gt__(self, other):
        return self.age > other.age
    

ali = Person("Ali", 27)
amir = Person("Amir", 29)

print(ali)
print(amir)

print("Ali age is greater than Amir?", ali > amir)
print("Amir age is greater than Ali?", ali < amir)