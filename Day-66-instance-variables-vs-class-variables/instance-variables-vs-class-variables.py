class Employee:
  count = 0

  def __init__(self):
    Employee.count = Employee.count + 1
  
  @staticmethod
  def total():
    return Employee.count


employee1 = Employee()
employee2 = Employee()
employee3 = Employee()
employee4 = Employee()

print("Total Employees are:", Employee.count)

employee5 = Employee()

print("(Again after new object) The total Employees are:", Employee.count)
employee5.count = 2
print("Employees count for employee5 (which have own count):", employee5.count)
print("But Employees count for employee4 (which don't have own count):", employee4.count)


print()
print("Setting universale count by direct class to 10")
Employee.count = 10
print("Total Employees are:", Employee.count)
print("But Total Employees for employee 5 are (still):", employee5.count)
print("Total Employees for employee 4 are:", employee4.count)
