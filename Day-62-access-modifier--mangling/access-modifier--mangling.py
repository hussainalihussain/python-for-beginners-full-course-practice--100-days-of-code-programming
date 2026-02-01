# There is no public, private, protected etc. in python
# Everything in python is public
# Python just do mangling if a variable name is started from double underscores (__)
# mangling means the name is converted to underscore class name and then the variable name
# if a variable name is: __age and the class name is Employee then the __age after mangling will become _Employee__age


class Person:
  def __init__(self):
    self.__name = "Some Person"
  
  def __something(self):
    print("something to test")


person = Person()
# print(person.__name) # we can't access any variable defined using double underscores (__) directly as python doing mangling
print(person._Person__name) # but we can access it indirectly

# person.__something() # again can't access directly
person._Person__something() # but we can access it indirectly