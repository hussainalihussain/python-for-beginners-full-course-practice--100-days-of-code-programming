# try:
#   n = [1, 2, 3, 4]
#   index = int(input("Enter index to search: "))

#   print(f"This number found in list '{n[index]}'")
# except ValueError:
#   print("Invalid Input (Only integer value is allowed)!")
# except IndexError:
#   print("Out of range index!")
# finally:
#   print("Everything is completed 1!")

# print("Everything is completed 2!")



'''
The above program finall or normal print do the same things, but to see the actual purpose of
FINALLY
then see the following
'''

def fun1():
  try:
    n = [1, 2, 3, 4]
    index = int(input("Enter index to search: "))

    print(f"This number found in list '{n[index]}'")

    return True
  except ValueError:
    print("Invalid Input (Only integer value is allowed)!")

    return False
  except IndexError:
    print("Out of range index!")
    
    return False
  finally:
    print("Everything is completed 1!")

  print("Everything is completed 2!")



'''
finally will execute even if we have return statements
but the noraml print, which is:
print("Everything is completed 2!")
can't execute if we have return statement
'''


result = fun1()

print(f"Result: {result}")
