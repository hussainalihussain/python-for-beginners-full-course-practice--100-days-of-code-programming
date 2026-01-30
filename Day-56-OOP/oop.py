class Person:
  name = "Hussain"
  age = 31

  def info(self):
    print(f"{self.name} is {self.age} years old!")

# person1 = Person()

# print(f"{person1.name} is {person1.age} years old")


person2 = Person()
person2.name = "Ahmad"
person2.age = 32

person3 = Person()
person3.name = "Sahil"
person3.age = 49

person4 = Person()
person4.name = "Akbar Ali"
person4.age = 38


person2.info()
person3.info()
person4.info() 