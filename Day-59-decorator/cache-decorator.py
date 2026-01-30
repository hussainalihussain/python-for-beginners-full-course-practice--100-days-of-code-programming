import time

def cache(func):
  memory = {}

  def wrapper(id):
    if id in memory:
      return memory[id]
    
    name = func(id)
    memory[id] = name

    return name
  
  return wrapper



def some_calculation_sample(result):
  time.sleep(5)

  return result



@cache
def square(n):
  return some_calculation_sample(n * n)

print("square of 5")
square(5)

print("square of 5 again (this shouldn't take time as it is already in memory)")
square(5)

print("square of 5 again (this shouldn't take time as it is already in memory)")
square(5)

print("Square of 6")
square(6)



users = {
  1: "ahmad",
  2: "sahil",
  3: "jameel",
}

@cache
def get_user(id):
  try:
    print(f"{users[id]} user found at #{id}")
  except:
    print(f"no user found #{id}")

get_user(0)
get_user(1)