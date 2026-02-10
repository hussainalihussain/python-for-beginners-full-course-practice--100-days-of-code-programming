class Parent:
  def some_helper(self):
    print("Helper from parent!")
  
  def some_text(self):
    print("Welcome to some text of parent")

  def some_method(self):
    print("Welcome from parent!")


class Child(Parent):
  def some_text(self):
    print("Welcome to some text of child")

  def some_method(self):
    super().some_method()
    print("Welcome from child!")

c = Child()

c.some_helper()
c.some_text()
c.some_method()







# ### `super` (kid version 🧸)

# Imagine a **parent** and a **child** 👨‍👧

# * The **parent class** knows how to do some things
# * The **child class** wants to do *most* of the same things
#   **plus** a little extra

# 👉 **`super` means: “Ask my parent to help.”**

# ---

# ### What `super` is for

# When a class **inherits** from another class:

# * The child can **reuse** the parent’s code
# * `super` lets the child say:

# > “Hey parent, do your part first.”

# ---

# ### Tiny story 📖

# Parent knows how to:

# * put on shoes 👟

# Child wants to:

# * put on shoes 👟
# * then grab a backpack 🎒

# So the child says:

# > `super()` → “Parent, you do the shoes part.”

# ---

# ### Important idea 🧠

# * `super` = **go to the parent**
# * It avoids **copy-pasting code**
# * It keeps things **clean and polite**

# ---

# ### What `super()` really means (simple)

# It gives you **access to the parent class’s methods**.

# You’re not replacing the parent — you’re **building on top of it**.
