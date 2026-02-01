class Parent:
  def greet(self):
    print("Hello from Parent!")

class Child(Parent):
  def hi(self):
    print("Hi i am from Child!")

child = Child()
child.greet()
child.hi()
