################################################
##  the default mode is also 'r' (read) mode  ##
################################################

f = open('test-file.txt', 'r')

fileContent = f.read()
f.close()

print(fileContent)

# to open and then close automatically we can use this syntax:
with open('test-file.txt') as _f:
  print(_f.read())


# can't do this as it is in read mode
#f.write('sample text!')