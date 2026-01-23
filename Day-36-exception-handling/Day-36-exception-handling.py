n = input("Enter number (enter string to break): ")

# for i in range(1, 10):
#   print(f"{n} * {i} = {i * int(n)}")

# try:
#   for i in range(1, 10):
#     print(f"{n} * {i} = {i * int(n)}")
# except:
#   print("Invalid Number")

try:
  for i in range(1, 10):
    print(f"{n} * {i} = {i * int(n)}")
except ValueError:
  print("Invalid Number")

print()

a = [1, 2]

try:
  a[5]
  int(n)
except IndexError:
  print("Index Error")
except ValueError:
  print("Invalid Number")


print("End of the Program!")
