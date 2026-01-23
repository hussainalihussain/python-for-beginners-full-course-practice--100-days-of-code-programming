import math
'''
Fibonacci Sequence

F(0) = 0, F(1) = 1
and then
F(n) = F(n-1) + F(n-2)

i.e. 
F(4) = F(4-1) + F(4-2)
F(4) = F(3) + F(2)

where
F(3) = F(2)+F(1)
F(2) = F(1) + F(0)
F(2) = 1 + 0 = 1

so
F(3) = F(2) + F(1)
F(3) = 1 + 1 = 2

thus
F(4) = F(3) + F(2)
F(4) = 2 + 1
F(4) = 3


Sort description:
Fibonacci of a number is sum of Fibonacci of previous two numbers

so the following is the sequence:
0 1 1 2 3 5 8 13 21 34 ...

For full detail see:
https://en.wikipedia.org/wiki/Fibonacci_sequence
'''

'''
Lets create a function for finding a Fibonnaci of a number
'''
# ✅ Exercise 2 — Recursive Fibonacci
def fibonacci(n):
  '''Find Fibonnaci of a given number'''
  if (n == 0):
    return 0
  
  if (n == 1):
    return 1
  
  return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))

# ✅ Exercise 1 — Recursive Sum of Digits
# that returns the sum of digits of a number.
# sum_digits(12345) → 15
def sum_digits(n):
  '''Sum each digit of a given number'''
  reminder = n % 10
  divisible = n - reminder
  # newN = divisible / 10
  newN = math.floor(divisible / 10) # no need for floor but just to get integer

  if newN <= 1:
    return reminder + newN

  return reminder + sum_digits(newN)

n = 1569
n = 10
n = 9
n = 19
n = 105
n = 999
# print(n, 'sum:', sum_digits(n))

# ✅ Exercise 3 — Recursive Reverse String
# reverse("python") → "nohtyp"
def reverse(str):
  '''Get the reverse of a given string'''
  strLen = len(str)

  if strLen <= 1:
    return str
  
  index = strLen - 1

  return str[index] + reverse(str[:index])

# print(reverse(''))
# print(reverse('meat'))
# print(reverse('professional'))
# print(reverse('Hussain Ali'))



# 🔥 Recursion Quiz 1 — Count Zeros in a Number
# count_zeros(n)

# Examples:
# count_zeros(10203040) → 4
# count_zeros(90009)    → 2
# count_zeros(7)        → 0


def get_last_digit(n):
  return n % 10

def trim_last_digit(n):
  return n // 10


'''
we need todo this:
* get the current digit
* current digit is 0
* count 1 and call with
'''

def count_zeros(n):
  '''Find the number of zeros in a given number'''
  reminder = n % 10
  newN = n // 10

  count = 1 if reminder == 0 else 0

  if newN == 0:
    return count
  
  return count + count_zeros(newN)





n = 101012034
n = 10
n = 111
print(n, 'zeros counts:', count_zeros(n))




# 🔥 Recursion Quiz 2 — Power Function
# power(a, b)

# Examples:
# power(2, 5) → 32
# power(3, 3) → 27
# power(5, 0) → 1

# 📌 Hint:
# a^b = a * a^(b-1)
# Stop when b == 0.


def power(n, pwr):
  '''Find the power/exponential of a given number'''

  # speical case 1, e.g. 0 ** 0 = undefined
  if (pwr == 0 and n ==0):
    return None

  # special case 2, e.g. 2 ** 0 = 1
  if (pwr == 0):
    return 1

  return n * power(n, pwr - 1)

n = 2
n = 5
n = 0
pwr = 0
# pwr = 1
# pwr = 2
# pwr = 3
# pwr = 4
# pwr = 5
# pwr = 6
# print(f"{n}***{pwr} =", power(n, pwr))
  



# 🔥 Recursion Quiz 3 — Check if String is Palindrome
# is_palindrome(s)

# Examples:
# "madam" → True
# "level" → True
# "python" → False
# "racecar" → True

# 📌 Hint:
# Check first and last character, then recurse on the middle part.

def is_palindrome(s):
  length = len(s)
  
  if length <= 1:
    return True

  if (s[0] != s[length - 1]):
    return False
  
  return is_palindrome(s[1:length-1])

str = 'level'
str = 'abcde'
str = 'madam'
str = 'lool'
str = 'pool'
str = 'cooc'
str = 'a'
print(str, 'is a palindrome string?', is_palindrome(str))