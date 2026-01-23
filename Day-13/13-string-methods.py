# Strings are immutable
# when we do something like:
 # a = "GOOD"
 # a.lower()
# then a.lower() create copy of "GOOD" but don't change the actual "GOOD"


# lower
a = "Something New"
print(a.lower())

# upper
print()
print("This is Upper".upper())

# capitalize
print()
title = "introduction to python"
print('capitalize of', '"' + title + '":', title.capitalize())

# title
print()
name = "hussain ali"
print('title of', '"' + name + '":', name.title())

# endswith
print()
print('"' + name + "'", 'ends with', '"ali"?', name.endswith('ali'))
print('"' + name + "'", 'ends with', '"hussain"?', name.endswith('hussain'))

# startswith
print()
print('"' + name + "'", 'starts with', '"ali"?', name.startswith('ali'))
print('"' + name + "'", 'starts with', '"hussain"?', name.startswith('hussain'))

# rstrip
print()
string = "!!!welcome to the show!!!!"
print('string:', string)
print('rstrip of "!":', string.rstrip('!'))

# lstrip
print()
print('string:', string)
print('lstrip of "!":', string.lstrip('!'))

# replace
print()
sentance = "Hi, Ali how are you. Ali should we go? ali!"
replaceWith = "Hussain"
print("Sentance:", sentance)
print("Replacing by", replaceWith + ':')
print(sentance.replace("Ali", replaceWith))

# split
print()
names = "Hussain,Ali,Amir,Zohaib,Usama,Mukshif,Nabeel"
print("String:", names)
print("After Split:", names.split(","))

# center
print()
string = "Hi, everyone!"
print("String:", string)
print("Centering:")
print(string.center(20))

# count
print()
sentance = "Hi, Ali how are you. Ali should we go? ali!"
toFind = "Ali"
print("Sentance:", sentance)
print("Total", sentance.count(toFind), "times", '"' + toFind + '"', "appeared in the sentance!")


# find
print()
sentance = "Hi, Ali how are you. Ali should we go? ali!"
toFind = "Ali"
toFind = "Ali2"
print("Sentance:", sentance)
print("Position of", '"' + toFind + '"', 'in the sentence:', sentance.find(toFind))


# index
print()
sentance = "Hi, Ali how are you. Ali should we go? ali!"
toFind = "Ali"
# toFind = "Ali2"
print("Sentance:", sentance)
print("Position of", '"' + toFind + '"', 'in the sentence:', sentance.index(toFind))

# isalphanum


# isalpha
# islower
# isupper
# isprintable
# isspace
# istitle
# swapcase
print()
sentance = "Hussain Ali"
print("Swapping Case:", sentance.swapcase())
print("Swapping Case:", sentance.swapcase().swapcase())
