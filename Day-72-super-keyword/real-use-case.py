class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id
  
  def info(self):
    print(f"#{self.id} - {self.name}")

class Developer(Employee):
  def __init__(self, name, id, lang):
    super().__init__(name, id)
    self.lang = lang
  
  def info(self):
    super().info()
    print(f"Language: {self.lang}")
  


e = Employee("Ahmad", "253")
e.info()

print()
print()

d = Developer("Hussain", "123", "Python")
d.info()