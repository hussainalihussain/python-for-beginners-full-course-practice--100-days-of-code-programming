class Employee:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return f"Employee({self.name})"

e = Employee("Hussain")
print(e)


# this time repr will not call
# but
# there is a way to call it
class Employee2:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return f"Employee2({self.name})"

  def __str__(self):
    return f"Employee name lenghth: {len(self.name)}"

e = Employee2("Hussain")
print(e)
print(repr(e))