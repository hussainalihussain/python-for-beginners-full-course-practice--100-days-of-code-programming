class MainEmployee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  
  def info(self):
    print(f"{self.name} takes {self.salary} salary!")
    print()


employee1 = MainEmployee("Hussain", 25000)
employee1.info()

employee2String = "Ahmad: 15000"
employee2 = MainEmployee(employee2String.split(":")[0], int(employee2String.split(":")[1]))
employee2.info()




print("But a more and better option is to use Class method as alternative constructor")
print()

class Employee(MainEmployee):
  # Alternative Constructors
  @classmethod
  def from_string(cls, string):
    return cls(string.split(":")[0], int(string.split(":")[1]))

  @classmethod
  def from_list(cls, list):
    return cls(list[0], list[1])


employee3 = Employee.from_string("Sohail Ahmad: 18000")
employee3.info()

employee4 = Employee.from_list(["Jamal Khan", 22500])
employee4.info()


print("Lets see another example")
print()

class User:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
  
  def info(self):
    print(f"First name: {self.first_name} and last name: {self.last_name}")
  
  @classmethod
  def from_fullname(cls, fullname):
    return cls(fullname.split(" ")[0], fullname.split(" ")[1])

u1 = User.from_fullname("Hussain Ali")
u1.info()