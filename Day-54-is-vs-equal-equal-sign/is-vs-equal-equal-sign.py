# is: exact location of object in memory
# ==: same value

# example:
# Ahmad have iphone 17 (just bought right now)
# Wali have iphone 17 (he also bought right now)
# ahmad iphone 17 == wali iphone 17 => true
# ahmad iphone 17 is wali iphone 17 => no -> not the same (these are two different phones not a single one)

# for Truthy "is"
# Ahmad iphone 17 -> (1)
# Ahmad iphone just got it now -> (2)
# here as both are indicatating to a same phone
# this means
# (1) is (2) => true

# Another Example:
# If Ahmad drop his phone and now broken
# this doesn't means that the Wali phone is also broken

# Another Example
# Lets say Ahmad is an english teacher
# if we say Ahmad's phone
# OR say
# english teacher phone
# both are indicating to a same phone
# this means the 'is' here will be true

print("### List")
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # false (as a and b are stored in different places in the memory)
print(a == b) # true (as both values are same)


# but here is another example
print("\n### Integer")
a = 6
b = 6

print(a is b) # true (as 6 is a constant i.e., immutable so python didn't take a separate memory location for each as to reduce the memory)
print(a == b) # true (as both values are same)

# see the similar examples:


# see the similar examples:
# string
print("\n### String")
a = "hello"
b = "hello"

print(a is b) # true (constant/immutable)
print(a == b) # true (as both values are same)

# Tuples (tuples are immutable)
print("\n### Tuple")
a = (1, 2)
b = (1, 2)

print(a is b) # true (as tuples are immutable)
print(a == b) # true (as both values are same)

print("\n### Tuple (different)")
a = (1, 2)
b = (2, 3)
print(a is b) # false (tuples are immutable but the values are not same so python will take completely separate memory spaces for each)
print(a == b) # false (as both values are different)

# for None
print("\n### None")
a = None
b = None

print(a is b) # true
print (a is None)
print(a == b) # true