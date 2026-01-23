countries1 = ("Pakistan", "Afghanistan", "Iran")
countries2 = ("India", "Bangladesh")

allCountries = countries1 + countries2

print(countries1)
print(countries2)
print('All countries:')
print(allCountries)
print('total countries: ', len(allCountries))


print()
set = (1, 2, 0, 1, 5, 1, 2, 7)

print(set.count(1))

print(set.index(1))

# index(searchFor, startFromIndex, endToIndex)
print(set.index(1, 1))

print(set.index(1, 4, 6))



list = list(set)
print(type(list))