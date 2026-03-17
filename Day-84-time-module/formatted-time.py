import time

localTime = time.localtime()

formattedTime = time.strftime("%Y-%m-%d %H:%M:%S")

print(formattedTime)

formattedTimeWithAmPm = time.strftime("%Y-%m-%d %I:%M:%S %p")

print(formattedTimeWithAmPm)
