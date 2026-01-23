dict = {
  "affect": "To influence or cause a change in something or someone.",
  "decide": "To make a choice or judgment about something after thinking about it.",
  "develop": "To grow or cause to grow and become more advanced.",
  "knowledge": "Understanding of a subject that you get by experience or education.",
  "value": "The importance, worth, or usefulness of something.",
}

# print("Type:")
# print(type(dict))
# print()

'''
1. Accessing values
'''
# print(dict['affect'])
# print(dict.get('develop'))

# key not exists
# print(dict['purpose']) # will generate error
# print(dict.get('purpose'))

'''
2. get keys
'''
# print(dict.keys())

# print("\nLoop using dict.keys()")
# # loop throught
# for key in dict.keys():
#   print(f"{key}: {dict[key]}")

# print("\nLoop directly")
# # loop directly
# for value in dict:
#   print(value)

'''
3. get values
'''
# print(dict.values())

# print()
# print("Accessing using dict.values()")

# for value in dict.values():
#   print(value)

'''
4. get items
'''


print(dict.items())

print()
print("Accessing using dict.items()")

for key, value in dict.items():
  print(f"{key}: {value}")