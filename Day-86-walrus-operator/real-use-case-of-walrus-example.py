# No use of Walrus operator code

fruits = list()

# No Walrus operator code
# while True:
#   new_fruit = input("Fruit name: ")

#   if new_fruit == "quit":
#     break

#   fruits.append(new_fruit)



# Code with Walrus operator
while (new_fruit:=input("Fruit name: ")) != "quit":
  fruits.append(new_fruit)


print()

print("Your fruits list:")

for fruit in fruits:
  print(f"* {fruit}")
