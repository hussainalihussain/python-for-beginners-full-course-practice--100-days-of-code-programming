from functools import reduce

numbers = [1, 2, 3, 4, 5]

#map
doubleOfNumbers = list(map(lambda x: x*2, numbers))
print(doubleOfNumbers)

square = lambda x: x * x
squareOfNumbers = list(map(square, numbers))
print(squareOfNumbers)


#filter
names = ['ahmad', 'wali', 'ali', 'jamal']

def eligibleOrNot(name):
  return name != 'ali' and name != 'wali'

eligibleNames = list(filter(eligibleOrNot, names))
print(eligibleNames)


#reduce
numbers = [1, 2, 3, 4, 5]
# numbers = [1, 2, 3, 4, 5]
# 1. [3, 3, 4, 5]
# 2. [6, 4, 5]
# 3. [10, 5]
# 4. 15

sum = lambda x, y: x+y

total = reduce(sum, numbers)

print(total)
