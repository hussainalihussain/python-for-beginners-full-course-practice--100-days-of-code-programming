# explicit type casting
a = "2"
b = "3"

print(a + b)



a = 2
b = 3

print(a + b)



print("Solution for string (but having int inside) variables")
a = "2"
b = "3"
print("Type of ", a, ": ", type(a))
print("Type of ", b, ": ", type(b))
print("Sum of ", a, "and", b)
print(int(a) + int(b))





a = "2.5";
b = "3"

print(float(a) + int(b))









# implicit type casting

n1 = 5.5
n2 = 2

print("Type of", n1, ':', type(n1))
print("Type of", n2, ':', type(n2))
n3 = n1 + n2
print("Result sum:", n3, "(Where its type:", type(n3), ")")
