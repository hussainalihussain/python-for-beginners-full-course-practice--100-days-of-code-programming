name = "Hussain"

for character in name:
  print(character, end=",")

print()

# List
print()
print("Loop through list")
listOfFruits = ["apple", "banana", "mango"]

for fruit in listOfFruits:
  print(fruit)

# loop within loop
print()
print("Loop within loop")

for fruit in listOfFruits:
  print("Fruit:", fruit)

  for character in fruit:
    print(character)


# Range
print()
print("Loop using range(5)")

for n in range (5):
  print(n)

print("Loop using range(5) - manually handling start")

for n in range (5):
  print(n + 1)

print("Loop using range(1, 6)")

for n in range(1, 6):
  print(n)

print("Loop using range(1, 12, 3)")

for n in range(1, 12, 3):
  print(n)

print("Loop using range(1, 20, 4)")

for n in range(1, 20, 4):
  print(n)




