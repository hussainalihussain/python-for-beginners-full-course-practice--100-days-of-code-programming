# 📊 5. IoT / Sensor Data
# Scenario:
# * Temperature readings
# * Convert °C → °F
# * Filter abnormal readings (>100°F)
# * Find max temperature
#
# 📌 Use case: Smart devices, weather monitoring

from functools import reduce


celsius_to_fahrenheit = lambda c: c * 1.8 + 32
abnormal_readings = lambda f: f > 100
def max_temprature (tempf_1, tempf_2):
  return tempf_1 if tempf_1 > tempf_2 else tempf_2

temps_c = [30, 35, 40, 42, 28]

temps_f = list(map(celsius_to_fahrenheit, temps_c))

abnormal_f = list(filter(abnormal_readings, temps_f))

max_temprature = reduce(max_temprature, abnormal_f)

print('max temprature: ', max_temprature)














# Chatgpt written code

# from functools import reduce

# temps_c = [30, 35, 40, 42, 28]

# temps_f = map(lambda c: (c * 9/5) + 32, temps_c)
# high_temps = filter(lambda f: f > 100, temps_f)
# max_temp = reduce(lambda a, b: a if a > b else b, high_temps)

# print(max_temp)
