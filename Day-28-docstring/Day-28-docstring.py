def square(n):
  '''take input n and return the square of that number'''

  return n**2

print(square(4))

print(square.__doc__)

def sum(n1, n2):
  print('\n')
  '''this is not docstring'''

  return n1 + n2

print(sum(1, 2))
