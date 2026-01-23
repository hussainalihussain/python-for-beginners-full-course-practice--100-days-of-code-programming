i = 0;

while i < 6:
  print(i)
  i = i+1

print()


max = 10

while i >= 0:
  print(i)
  i = i - 1;



print()

fruit = input("Name of fruit (banana, apple, mango) to find price: ")
print(fruit)

while fruit != 'banana' and fruit != 'apple' and fruit != 'mango':
  fruit = input("Name of fruit (banana, apple, mango) to find price: ")
  print(fruit)

match fruit:
  case 'banana':
    print("Banana price is", 200, "per dozen!")
  case "apple":
    print("Apple price is", 300, "per KG!")
  case _ if (fruit == "mango"):
    print("Mango price is", 380, "per KG!")


print()
print("Else with while")

i = 2

while i <= 6:
  print ("i:",i)
  i = i + 1
else:
  print("While loop is ended!")

print()

while False:
  print("Non executable code")
else:
  print("Else of while loop")

