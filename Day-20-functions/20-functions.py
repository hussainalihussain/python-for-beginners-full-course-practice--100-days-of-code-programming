def sum(n1, n2):
  result = n1 + n2

  print("Sum of", n1, "and", n2, "is", result)


sum(1, 3)
sum(5, 20)



def avg(a=5,b=5):
  res = a + b

  print("Average:", res / 2)

avg()
avg(3, 9)
avg(3)
# avg(a=3) # same as avg(3)
avg(b=11)


def power(num, power = 2):
  res = num ** power
  
  print("Power:", res)

power(2)
power(2, 3)
power(2, 5)




def average(*numbers):
  print("Type of args:", type(numbers))
  sum = 0

  for number in numbers:
    sum = sum + number
  
  print("Calculated Average:", sum / len(numbers))

average(6, 10, 20)

def fun(**objects):
  print("Type of arg:", type(objects))
  
  for object in objects:
    print("Object:", object)

fun(name="Hussain", age=23, position="Project Manager")