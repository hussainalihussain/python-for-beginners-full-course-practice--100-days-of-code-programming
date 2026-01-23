'''
###############
# Explanation #
###############

Hussain
0123456
total length = 7
say if we want -1 then
7-1 = 6
6th position = n

if it is -3 then
7-3 = 4
4th position = a
and upto end i.e, if we have [-3:]
'''

name = "Hussain"

print('Full Name:', name)

# [n]
print('5th:', name[4])

# [n:]
print('[4:]', name[4:])

# [:m]
print('[:5]', name[:5])

# [n:m]
print('[1:4]', name[1:4])

#[0:]
print('[0:]', name[0:])

#[:len(name)]
print('[:len(name)]', name[:len(name)])

# [:]
print('[:]', name[:])

# [0:len(name)]
print('[0:len(name)]', name[0:len(name)])

#[:len(name)]
print('[:len(name)]', name[:len(name)])

# [-n:]
print('[-1:]', name[-1:])
print('[-3:]', name[-3:])

# [len(name)-n:]
print('[len(name)-1:]', name[len(name)-1:])
print('[len(name)-3:]', name[len(name)-3:])

# [:-m]
print('[:-1]', name[:-1])
print('[:-3]', name[:-3])

# [:len(name)-m]
print('[:len(name)-1]', name[:len(name)-1])
print('[:len(name)-3]', name[:len(name)-3])

# [-n:-m]
print('[-4:-1]', name[-4:-1])

# [-n:m]
print('[-3:6]', name[-3:6])

# [n:-m]
print('[2:-2]', name[2:-2])


# Quick Quiz
# nm = "Harry"

# print(nm[-4:-2]) # it should print: ar