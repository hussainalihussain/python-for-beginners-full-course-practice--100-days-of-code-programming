amount = int(input("Enter your budget: "))

if (amount < 50):
  print("Ohh no, nothing is possible to buy!")
elif (amount < 100):
  print("You can buy some or one biscuits!")
else:
  print("You amount is greater than 100, you can buy more items")