str1 = "Hi, everyone"
str2 = 'Welcome to the ITO office!'
str3 = 'This is ali\'s phone'
str4 = "This is ahmad's phone"
str5 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
Etiam imperdiet eget odio ac vulputate. Nulla eget erat consequat sem commodo \
suscipit. Etiam pretium ut erat vitae cursus. Etiam mollis purus quis elit congue posuere.\
Nam gravida blandit nulla eget scelerisque. \
Donec placerat arcu ut libero egestas, sed commodo odio cursus."
str6 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Etiam imperdiet eget odio ac vulputate. Nulla eget erat consequat sem commodo 
suscipit. Etiam pretium ut erat vitae cursus. Etiam mollis purus quis elit congue posuere.
Nam gravida blandit nulla eget scelerisque. 
Donec placerat arcu ut libero egestas, sed commodo odio cursus.
"""
str7 = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Etiam imperdiet eget odio ac vulputate. Nulla eget erat consequat sem commodo 
suscipit. Etiam pretium ut erat vitae cursus. Etiam mollis purus quis elit congue posuere.
Nam gravida blandit nulla eget scelerisque. 
Donec placerat arcu ut libero egestas, sed commodo odio cursus.
'''
name = "Hussain"


print(str7)

print("first character of name:", name[0])
print("second character of name:", name[1])
print("fifth character of name:", name[4])


print("\nPrinting characters one by one:")

for character in name:
  print(character)