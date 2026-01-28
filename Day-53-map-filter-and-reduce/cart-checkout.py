# 🛒 2. E-Commerce Cart Checkout
# Scenario:
# * Prices in cart
# * Apply 18% GST
# * Keep items above ₹500
# * Calculate total bill
#
# 📌 Use case: Online shopping checkout systems

from functools import reduce

applyGst = lambda amount: amount + amount * 0.18
sum = lambda x, y: x+y

cart_prices = [299, 799, 1200, 450, 999]

cart_prices_after_gst = list(map(applyGst, cart_prices))

total_bill = reduce(sum, cart_prices_after_gst)

print('cart prices: ', cart_prices)
print('cart prices (after GST): ', cart_prices_after_gst)
print('Total Bill: ', total_bill)