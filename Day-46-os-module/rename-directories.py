import os

# 2. Rename all these Module 1 - Module 100 with this names Practice 1 - Practice 100

directory = 'data'

for number in range(1, 101):
  oldPath = f"{directory}/Module {number}"
  newPath = f"{directory}/Practice {number}"

  if (not os.path.exists(newPath)):
    os.rename(oldPath, newPath)
