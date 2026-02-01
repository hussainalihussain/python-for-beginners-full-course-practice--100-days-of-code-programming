class Person:
  def __init__(self, name):
    self._name = name
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    self._name = name


class Employee:
  def __init__(self, position):
    self._position = position
  
  @property
  def position(self):
    return self._position

  @position.setter
  def position(self, position):
    self._position = position


wali = Person("Ali")
print(f"Name of the person is {wali.name}")

wali.name = "Wali"
print(f"Now the name of the person is {wali.name}")

print()

employee = Employee("junior web developer")
print(f"His position is {employee.position}")

employee.position = "web developer"
print(f"He promoted to {employee.position}")