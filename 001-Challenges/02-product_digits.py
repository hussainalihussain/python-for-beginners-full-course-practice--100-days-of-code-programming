'''
🔥 Recursion Quiz 5 — Product of Digits

Write a function:
product_digits(n)

Examples:

product_digits(123) → 6    (1*2*3)
product_digits(405) → 0    (4*0*5)
product_digits(7)   → 7
'''

def product_digits(n):
  if n < 10:
    return n

  digit = n % 10
  newN = n // 10

  return digit * product_digits(newN)

n = 123
n = 405
n = 7
n = 11111
n = 12112
n = 12212
print(f"{n}:", product_digits(n))



'''
🔥 Recursion Quiz 6 — Count Nested Lists

Given a list that may contain numbers or lists inside lists, count how many integers it contains.
def count_nested(lst)

Examples:

count_nested([1, 2, 3]) → 3

count_nested([1, [2, 3], 4]) → 4

count_nested([1, [2, [3, 4], 5], 6]) → 6

count_nested([]) → 0

📌 Hint:
If item is a list → recurse
Else → count + 1

'''

def count_nested(list):
  if len(list) == 0:
    return 0
  

