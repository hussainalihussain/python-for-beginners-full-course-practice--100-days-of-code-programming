# Magic method __str__

class Employee:
  name = "Hussain"

e = Employee
print(e)



class Employee2:
  name = "Hussain"

  def __str__(self):
    return f"Employee name is {self.name}"

e = Employee2()
print(e)




class Employee3:
  name = "Hussain"

  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"The Employee name is {self.name}"


e = Employee3("Hussain")
print(e)