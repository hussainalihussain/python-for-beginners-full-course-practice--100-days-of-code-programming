# Tuples are same as list except:
# Tuples are immutable

tup = (1, 5, 8)

print('tuple:', tup, len(tup))

wrongTup = (2)
rightTup = (2,)

print('type:', type(wrongTup))
print('type:', type(rightTup))


# tup[0] = 125 # will generate error

print('Acessing tuple....')
print(tup[0])
print(tup[2])
# print(tup[23423]) # index out of range error

