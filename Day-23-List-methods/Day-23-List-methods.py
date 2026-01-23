l = [21, 2, 22, 1, 3, 5, 8, 1, 2, 1]

print(l)

# add to end
# l.append(23)

# print(l)


# sort
# l.sort()

# print(l)

# re-verse
# l.reverse()

# print(l)


# duplicate
# see the problem:
# m = l
# l[0] = 0; # it will change the l[0] too
# print(m)
# print(l)

# the solution is to use copy()
# m = l.copy()
# m[0] = 0
# print(m)
# print(l)

# add item in b/w
# l.insert(2, 23)

# print(l)


# merge => add one list to the end of another list - TWO WAYs
n = [-1, -5, 0, -3]

# # first way
# o = l + n

# # even we can do this:
# # l = l + n

# print(o)

# second way:
l.extend(n)

print(l)


