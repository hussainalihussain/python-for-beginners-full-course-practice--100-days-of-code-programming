import os

# 1. create 100 directories 1-100 inside data directory, something like Os Module 1, Os Module 2, .... Module 100

directory = 'data'

if (not os.path.exists(directory)):
  os.mkdir(directory)

for number in range(1, 101):
  newDirectory = f"Module {number}"
  newDirectoryFullPath = f"{directory}/{newDirectory}"

  if (not os.path.exists(newDirectoryFullPath)):
    os.mkdir(newDirectoryFullPath)
  
  if number == 10:
    # Ignore the open (how it works) for now (just copy pasted from AI)
    os.open(f"{newDirectoryFullPath}/sample-text-file.txt", os.O_CREAT | os.O_WRONLY)


# 2. Rename all these Module 1 - Module 100 with this names Practice 1 - Practice 100
# see the rename-directories.py

# 3. get current working directory
# see working-directories.py

# 4. set current working directory
# see working-directories.py
