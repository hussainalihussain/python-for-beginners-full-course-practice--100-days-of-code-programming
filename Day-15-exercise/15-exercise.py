import time

currentHour = int(time.strftime('%H'))

# Say the following based on current time
# Good Morning
# Good Afternoon
# Good Evening

# Morning 1-12 am
# Afternoon 12-16 pm
# Evening 16-24

if (currentHour <= 12):
  print("Good Morning")
elif (currentHour <= 16):
  print("Good Afternoon")
else:
  print("Good Evening")