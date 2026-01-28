from functools import reduce


interest_rate = 12

principals = [1000, 2500, 4000, 1500]

get_with_interest = lambda amount: amount + amount * (interest_rate / 100)
sum = lambda a, b: a+b

with_interest = list(map(get_with_interest, principals))
total_amount = reduce(sum, principals)
total_with_interest_amount = reduce(sum, with_interest)

print('total amount: ', total_amount)
print('total amount (with interest): ', total_with_interest_amount)