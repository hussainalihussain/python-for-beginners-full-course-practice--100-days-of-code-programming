Perfect 😄 let’s go **super slow, super simple, like explaining to a child**.
Imagine I’m sitting next to you with crayons 🖍️

---

## 🌟 First… what is a decorator?

### Real-life idea:

You have a **gift** 🎁
You **wrap it with paper** 🎀
The gift is the same, but now it looks better or does more.

👉 **Decorator = gift wrapper for a function**

The function stays the same.
The decorator **adds extra behavior**.

---

## 🧠 Think of a function as a button

```python
def say_hi():
    print("Hi")
```

When you press the button → it says “Hi”

Now you want:

* Something to happen **before**
* Something to happen **after**

But you don’t want to change the button itself ❌

So… we **wrap** it!

---

# 🧩 Example 1: Logging (telling what’s happening)

### Real life:

Mom writes in a notebook:

> “Child started homework at 6pm”

---

### Step 1: The decorator

```python
def log_action(func):
```

👉 This function **receives another function**

```python
    def wrapper():
```

👉 This is the **new wrapped version**

```python
        print("Function is starting")
```

👉 Do something BEFORE

```python
        func()
```

👉 Call the original function

```python
        print("Function finished")
```

👉 Do something AFTER

```python
    return wrapper
```

👉 Give back the wrapped function

---

### Step 2: Use it

```python
@log_action
def play():
    print("Playing game")
```

Python secretly does this:

```python
play = log_action(play)
```

---

### When you run:

```python
play()
```

🖨️ Output:

```
Function is starting
Playing game
Function finished
```

🎉 The function got **superpowers**!

---

# 🧩 Example 2: Login check (security guard 👮)

### Real life:

You can’t enter school unless you have an ID card.

---

### Decorator

```python
def login_required(func):
```

Decorator receives a function

```python
    def wrapper(user):
```

Wrapper receives the user

```python
        if not user["logged_in"]:
            print("Go away! Login first!")
            return
```

👉 Stop if not logged in

```python
        func(user)
```

👉 Call original function

```python
    return wrapper
```

---

### Use it

```python
@login_required
def open_dashboard(user):
    print("Dashboard opened!")
```

---

### Try it

```python
user = {"logged_in": False}
open_dashboard(user)
```

🖨️ Output:

```
Go away! Login first!
```

---

# 🧩 Example 3: Timer (stopwatch ⏱️)

### Real life:

You time how long homework takes.

---

```python
import time
```

```python
def timer(func):
```

```python
    def wrapper():
        start = time.time()
```

👉 Start stopwatch

```python
        func()
```

👉 Do the work

```python
        end = time.time()
```

👉 Stop stopwatch

```python
        print("Time taken:", end - start)
```

```python
    return wrapper
```

---

### Use it

```python
@timer
def homework():
    time.sleep(2)
```

---

### Run

```python
homework()
```

🖨️ Output:

```
Time taken: 2.00
```

---

# 🧩 Example 4: Retry (don’t give up 💪)

### Real life:

If door doesn’t open, try again.

---

```python
def retry(times):
```

Decorator WITH settings

```python
    def decorator(func):
```

Receives function

```python
        def wrapper():
            for i in range(times):
                try:
                    func()
                    return
                except:
                    print("Try again")
```

```python
        return wrapper
    return decorator
```

---

### Use it

```python
@retry(3)
def open_door():
    print("Door opened")
```

---

# 🧩 Example 5: Checking numbers (rules 📏)

### Real life:

Teacher says:

> “Only positive numbers allowed!”

---

```python
def positive_only(func):
```

```python
    def wrapper(num):
        if num <= 0:
            print("Nope!")
            return
```

```python
        func(num)
```

```python
    return wrapper
```

---

### Use it

```python
@positive_only
def deposit(amount):
    print("Deposited", amount)
```

---

# 🧩 Example 6: Remembering answers (memory 🧠)

### Real life:

You remember math answers so you don’t redo them.

---

```python
def cache(func):
    memory = {}
```

```python
    def wrapper(n):
        if n in memory:
            print("I remember!")
            return memory[n]
```

```python
        result = func(n)
        memory[n] = result
        return result
```

```python
    return wrapper
```

---

### Use it

```python
@cache
def square(n):
    return n * n
```

---

## 🎯 FINAL MAGIC SENTENCE (Remember this!)

> **A decorator is a function that takes another function, wraps it, and adds extra behavior without changing the original function.**

---

If you want, next we can:

* Draw a **step-by-step flow**
* Practice writing ONE together
* Do a **quiz** (fun, promise!)
* Explain `*args` and `**kwargs` like Lego blocks 🧱

Just tell me 😊
