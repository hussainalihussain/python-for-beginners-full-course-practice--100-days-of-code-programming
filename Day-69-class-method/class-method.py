class Employee:
  company = "Tesla"

  def show(self):
    print(f"{self.name} is working in {self.company}")
  
  def changeCompany1(cls, newCompany):
    cls.company = newCompany
  
  @classmethod
  def changeCompany2(cls, newCompany):
    cls.company = newCompany


emp = Employee()
emp.name = "Hussain"
emp.show()
print("Class own company name:", Employee.company)

print()

emp.changeCompany1("Microsoft")
emp.show()
print("Class own company name:", Employee.company)

print()
emp.changeCompany2("Apple")
emp.show()
print("Class own company name:", Employee.company)
