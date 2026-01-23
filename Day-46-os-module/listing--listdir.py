import os

lookupDirectory = 'data'

# print(os.listdir(lookupDirectory))

# for directory in os.listdir(lookupDirectory):
#   print(directory)

for directory in os.listdir(lookupDirectory):
  print(directory)

  print(os.listdir(f"{lookupDirectory}/{directory}"), '\n')