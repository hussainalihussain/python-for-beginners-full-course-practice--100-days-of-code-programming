class Camera:
  def take_photo(self):
    print("Photo taken!")

class Phone:
  def call(self):
    print("Calling...")

class SmartPhone(Camera, Phone):
  def __init__(self):
    self._name = ''

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    self._name = name

  def info(self):
    print(f"Smart phone name: {self._name}")

samsung = SmartPhone()
samsung.name = "Samsung Galaxy A54 5G"

print("Information of the smart phone:")
samsung.info()
print()

print("Lets take photo by the phone")
samsung.take_photo()
print()

print("Lets call")
samsung.call()
print()
