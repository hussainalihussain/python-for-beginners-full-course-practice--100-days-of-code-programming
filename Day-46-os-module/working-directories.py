import os

# 3. get current working directory
print(os.getcwd())

directoryToCreate = 'test-directory-created-with-os-module'

if (not os.path.exists(directoryToCreate)):
  os.mkdir(directoryToCreate)


# 4. set current working directory
os.chdir("C:\\xampp\\htdocs\\LEARNing\\PYTHON\\Play-all-Python-for-Beginners-Full Course)-100DaysOfCode-Programming")

if (not os.path.exists(directoryToCreate)):
  os.mkdir(directoryToCreate)