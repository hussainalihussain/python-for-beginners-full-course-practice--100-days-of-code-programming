userInput = input("Enter number b/w 1 and 10 (get Fruit): ")


def fun1():
  if userInput == 'quit':
    return

  n = int(userInput)

  if n < 1 or n > 10:
    raise ValueError("Invalid input!")

  choices = [
    "Apple", 
    "Banana", 
    "Orange", 
    "Grapes", 
    "Mango", 
    "Pineapple", 
    "Strawberry", 
    "Watermelon", 
    "Peach", 
    "Cherry"
  ]

  print(f"Awesome your choice is {choices[n - 1]}")


fun1()