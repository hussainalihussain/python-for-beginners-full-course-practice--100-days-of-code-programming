class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def who(self):
    print(f"{self.name} is {self.age} years old!")
  

ahmad = Person("Ahmad", 32)


print(help(ahmad))

print()
print()

print(help("simple string!"))






# ### What is `help()`?

# **`help()` means: “Explain this to me, Python.”** 📖

# It’s like asking a **teacher** instead of just looking at buttons.

# ---

# ### Compare them 🧠

# * `dir(x)` → “What buttons does this thing have?”
# * `help(x)` → “What do these buttons actually *do*?”

# ---

# ### Example 🧁

# ```python
# help(str)
# ```

# Python explains:

# * what a `str` is
# * what it’s used for
# * lists methods **with explanations**

# Another one:

# ```python
# help("hello".upper)
# ```

# Python says:

# > “`upper()` makes all letters big.”

# ---

# ### When you run `help()`

# Sometimes you’ll see a long page of text.
# That’s normal. It’s a **manual** 📘

# To exit:

# * press **`q`**

# ---

# ### Tiny memory trick

# **`dir()` = list**
# **`help()` = explanation**