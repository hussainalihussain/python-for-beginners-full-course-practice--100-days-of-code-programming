class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def who(self):
    print(f"{self.name} is {self.age} years old!")
  

ahmad = Person("Ahmad", 32)

print(dir(ahmad))

print()
print()

print(dir("Something"))










# Imagine **Python is a big toy box**.

# Every toy (like a number, a list, or a function) is an **object**.
# Inside each toy are **little buttons and tricks** it can do.

# ### `dir()` is like asking:

# 👉 **“Hey toy, what buttons do you have?”**

# ---

# ### Example 🍭

# ```python
# dir("hello")
# ```

# Python looks at the word `"hello"` and says:

# > “Here’s **everything you can do** with this word!”

# It gives you a big list like:

# * `upper`
# * `lower`
# * `split`
# * and a bunch of weird names too 👀

# Those are the **buttons** you can press.

# ---

# ### Another example 🚗

# ```python
# my_list = [1, 2, 3]
# dir(my_list)
# ```

# Python says:

# > “Here are all the things a list knows how to do!”

# Like:

# * `append` (add a toy)
# * `pop` (take one out)
# * `sort` (put them in order)

# ---

# ### The weird names with `__` 🤖

# You’ll see stuff like:

# ```text
# __add__
# __len__
# ```

# Those are **secret robot buttons** 🦾
# Python uses them behind the scenes.
# You can ignore them for now. Totally fine.

# ---

# ### Tiny memory trick 🧠

# **`dir()` = “show me what this thing can do”**
