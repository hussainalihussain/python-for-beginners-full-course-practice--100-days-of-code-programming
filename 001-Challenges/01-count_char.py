'''
🔥 Recursion Quiz 4 — Count Occurrences of a Character

count_char(s, ch)
that returns how many times a character appears in a string.

Examples:

count_char("recursion", "r") → 2
count_char("banana", "a")    → 3
count_char("hello", "z")     → 0
'''


def count_char(string, character):
  strLen = len(string)

  matched = string[strLen - 1] == character
  counter = 1 if matched else 0

  if strLen == 1:
    return counter

  return counter + count_char(string[:strLen - 1], character)

print(count_char("recursion", "r"))
print(count_char("banana", "a"))
print(count_char("hello", "z"))