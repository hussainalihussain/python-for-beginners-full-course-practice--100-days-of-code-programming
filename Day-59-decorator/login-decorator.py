def auth(func):
  def wrapper(user):
    if not user['loggedin']:
      print("Please login first!")
      
      return

    func(user)

  return wrapper

@auth
def open_dashboard(user):
  print("Welcome to dashboard!")


ali = {"loggedin": False}
wali = {"loggedin": True}

open_dashboard(ali)
# open_dashboard(wali)