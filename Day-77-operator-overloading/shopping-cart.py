class Cart:
    def __init__(self, totalItems):
        self.totalItems = totalItems
    
    def __str__(self):
        return f"Total items in cart are {self.totalItems}"
    
    def __add__(self, other):
        return Cart(self.totalItems + other.totalItems)


cart1 = Cart(3)
print(cart1)

cart2 = Cart(5)
print(cart2)

print()
print("Sum of both carts......")
print(cart1 + cart2)