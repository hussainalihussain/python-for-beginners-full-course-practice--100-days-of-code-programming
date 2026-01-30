class Person:
  name = ""
  age = 0

  def __init__(self, name, age):
    print("Constructor called!")
    self.name = name
    self.age = age

  def info(self):
    print(f"{self.name} is {self.age} years old!")
  
person1 = Person("Hussain", 31)
person1.info()

person2 = Person("Ali", 28)
person2.info()