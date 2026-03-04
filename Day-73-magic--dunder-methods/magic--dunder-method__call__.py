class Employee:
  def __init__(self, name):
    self.name = name
  
  def __call__(self):
    print ("__call__ called")
  

e = Employee("Ali")
e()

