###############
#    Break    #
###############

# Do-While loop alternative in Python
# 'e' will be used to exit
while True:
  fruit = input("Name of fruit (banana, apple, mango) to find price: ")
  print(fruit)

  if fruit == 'banana' or fruit == 'apple' or fruit == 'mango' or fruit == 'e':
    break

match fruit:
  case 'banana':
    print("Banana price is", 200, "per dozen!")
  case "apple":
    print("Apple price is", 300, "per KG!")
  case _ if (fruit == "mango"):
    print("Mango price is", 380, "per KG!")
  case _:
    print('You skip the searching of price!')

###############
#   Continue  #
###############

for n in range (0, 11):
  if (n % 2 != 0):
    continue
  
  print(n)