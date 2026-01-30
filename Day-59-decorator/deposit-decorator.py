def only_positive(func):
  def wrapper(amount):
    if amount < 1:
      return
    
    func(amount)

  return wrapper

@only_positive
def deposit(amount):
  print(f"Deposited: {amount}")

deposit(0)
deposit(100)