def factorial(n):
  '''
    Find the factorial of a number
  '''
  if (n == 1 or n == 0):
    return 1
  
  return n * factorial(n - 1)

print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

'''
Explanation:
Factorial
factorial of 5:
= 5 * factorial (4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120

'''