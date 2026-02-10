class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def who(self):
    print(f"{self.name} is {self.age} years old!")
  

ahmad = Person("Ahmad", 32)


print(ahmad.__dict__)

print()
print()


# str = "Something..."
# print(str.__dict__)

# print()
# print()

# l = [1, 2, 3]
# print(l.__dict__)





# ### `__dict__`

# Think of an object as a **person** 🧍

# That person has:

# * a name
# * an age
# * a backpack with their own stuff

# 👉 `__dict__` is **the backpack** 🎒

# It shows **all the variables that belong to that object**.

# ---

# ### Example 🍎

# ```python
# class Person:
#     pass

# p = Person()
# p.name = "Sam"
# p.age = 7

# p.__dict__
# ```

# You’ll see:

# ```python
# {'name': 'Sam', 'age': 7}
# ```

# That means:

# > “These are the things this object remembers about itself.”

# ---

# ### Super important idea 🧠

# * `__dict__` = **data (facts)**
# * `dir()` = **abilities (actions + data)**

# So:

# * `dir(obj)` → *what it can do*
# * `obj.__dict__` → *what it has*

# ---

# ### Why numbers don’t work the same 🔢

# If you try:

# ```python
# x = 5
# x.__dict__
# ```

# It fails 😅
# Because numbers don’t carry backpacks — they’re **simple** objects.

# ---

# ### Tiny memory trick

# **`__dict__` = dictionary of an object’s stuff**






# Is __dict__ showing actions or stored data?

# ### **`__dict__` shows stored data** 🗂️

# Not actions.

# It’s the object’s **backpack of facts**, not its buttons.

# So:

# * **Actions** → methods (like `__add__`, `append`)
# * **Stored data** → `__dict__`

# 💡 Tiny mantra to remember:

# > **`__dict__` = data, `dir()` = abilities**
