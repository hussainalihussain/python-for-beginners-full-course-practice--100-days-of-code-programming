def retry(times):
  def decorator(func):
    def wrapper():
      for i in range(times):
        try:
          func()

          return
        except:
          print("Try again")
      
    return wrapper
  return decorator

@retry(3)
def open_door():
  print("Door opened")

open_door()