for i in range(5):
  print(i)
else:
  print("For loop Executed successfully")


print()

i = 0

while i < 5:
  i = i + 1
  print(i)
else:
  print("Else of while loop executed")

print()

print("Let do experiment with break inside loops")

for i in range(4):
  print(i)

  if (i > 2):
    break
else:
  print("For loop Executed successfully")


print()

i = 0

while i < 5:
  i = i + 1
  print(i)

  if i > 3:
    break
else:
  print("Else of while loop executed")