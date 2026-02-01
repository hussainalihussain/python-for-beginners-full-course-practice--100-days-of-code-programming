class Calculator:
  @staticmethod
  def sum(a, b):
    return a + b

calc = Calculator

print(calc.sum(2, 3))
print(Calculator.sum(5, 9))