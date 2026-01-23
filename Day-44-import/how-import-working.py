# 1
# import math

# print(math.pi)
# print(math.sqrt(9))

# 2
# import math as m

# print(m.pi)
# print(m.sqrt(16))

# 3
# from math import pi, sqrt

# print(pi)
# print(sqrt(25))

#4
# from math import pi as pii, sqrt

# print(pii)
# print(sqrt(81))


#5: Non recommended way (maybe can conflict with other variables and functions)
# from math import *

# print(pi)
# print(sqrt(100))

#6: Importing from our own file
# I.
# import welcome

# welcome.greeting()
# print(welcome.name)

# II.
# from welcome import greeting, name as whois

# greeting()

# print(whois)


# III. Again: this is a non recommended way
# from welcome import *
# greeting()

# print(name)


# IV.
import welcome as w

w.greeting()
print(w.name)