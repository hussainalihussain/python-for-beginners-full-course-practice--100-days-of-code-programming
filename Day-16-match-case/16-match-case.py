fruit = input("Enter fruit to find price (banana, apple, mango): ")

match fruit:
  case 'banana':
    print("Banana price is", 200, "per dozen!")
  case "apple":
    print("Apple price is", 300, "per KG!")
  case _ if (fruit == "mango"):
    print("Mango price is", 380, "per KG!")
  case "":
    print("Please enter a value!".center(30))
  case _:
    print("Price is not available for", fruit)