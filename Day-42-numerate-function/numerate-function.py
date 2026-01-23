fruits = ['apple', 'banana', 'strawberry', 'orange']


'''
What we do normally
'''
# index = 0

# for fruit in fruits:
#   print(f"{index}=> {fruit}")

#   index += 1


'''
An easy way is to use enumerate function
'''

for index, fruit in enumerate(fruits):
  print(f"{index}=> {fruit}")

print()

print("##############")
print("# Dictionary #")
print("##############")

dictionary = {
  "cat": "A small animal that says meow.",
  "dog": "A friendly animal that says woof.",
  "sun": "The bright ball in the sky that gives light.",
  "moon": "The round shape you see in the night sky.",
  "tree": "A tall plant with a trunk, branches, and leaves.",
  "ball": "A round object used to play games.",
  "book": "A thing you read that has pages.",
  "car": "A vehicle that people use to travel on roads.",
  "water": "A clear liquid that we drink.",
  "bird": "An animal with wings that can fly.",
}

for index, (word, meaning) in enumerate(dictionary.items(), start=1):
  print(f"{word}: {meaning}")