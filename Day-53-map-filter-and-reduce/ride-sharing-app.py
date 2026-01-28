# 🚗 4. Ride Sharing App (Uber / Ola Style)
# Scenario:
# * Distances (km)
# * Fare = ₹12/km
# * Trips longer than 5 km
# * Total earnings
#
# 📌 Use case: Driver payout calculation


from functools import reduce


distances = [2.5, 10, 6, 3, 15]

get_fare = lambda distance: distance * 12
get_longer = lambda distance: distance > 5
sum = lambda x, y: x + y

fares = list(map(get_fare, distances))
longer_distances = list(filter(lambda d: d > 5, distances))
total_earning = reduce(sum, fares)

print('distances: ', distances)
print('fares: ', fares)
print('longer distances: ', longer_distances)
print('total earning: ', total_earning)



































# Response of Chatgpt


# from functools import reduce

# distances = [2.5, 10, 6, 3, 15]

# fares = map(lambda d: d * 12, distances)
# long_trips = filter(lambda f: f > 60, fares)
# earnings = reduce(lambda x, y: x + y, long_trips)

# print(earnings)
