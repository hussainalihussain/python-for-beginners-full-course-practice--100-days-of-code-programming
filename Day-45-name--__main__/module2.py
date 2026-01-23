# The __name__ variable in Python is a special built-in variable that tells you the name of the current module
# * If the file is run directly as the main program, __name__ is set to the string "__main__".
# * If the file is imported as a module into another script, __name__ is set to the module's name (which is generally the filename without the .py extension). 


def helloWorld():
  print("Hello World!")

print(f"__name__: {__name__}")

if __name__ == '__main__':
  helloWorld()