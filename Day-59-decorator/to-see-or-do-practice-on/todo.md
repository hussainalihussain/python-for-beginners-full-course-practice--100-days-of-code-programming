A **decorator in Python** is a clean, readable way to **modify or extend the behavior of a function (or class) without changing its source code**.

Think of it as *wrapping* a function with extra logic 🎁

---

## Basic idea

Functions in Python are **first-class objects**, so you can pass them around and wrap them.

### Simple decorator example

```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
```

Use it like this:

```python
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### Output

```
Before function runs
Hello!
After function runs
```

`@my_decorator` is just syntactic sugar for:

```python
say_hello = my_decorator(say_hello)
```

---

## Decorator with arguments

Most real functions take parameters, so your decorator should handle them.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
```

---

## Preserving function metadata (`functools.wraps`)

Without this, the decorated function loses its name and docstring 😬

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## Real-world examples

### 1. Timing a function ⏱️

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper
```

---

### 2. Authorization / validation

```python
def require_login(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_logged_in:
            raise PermissionError("Login required")
        return func(user, *args, **kwargs)
    return wrapper
```

---

### 3. Decorators with their own arguments

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
```

Usage:

```python
@repeat(3)
def hello():
    print("Hi")
```

---

## Class decorators (quick mention)

```python
def add_repr(cls):
    cls.__repr__ = lambda self: f"<{cls.__name__}>"
    return cls
```

---

## TL;DR

* Decorators **wrap functions or classes**
* Use `@decorator_name`
* Use `*args, **kwargs` for flexibility
* Use `functools.wraps` to keep metadata
* Common uses: logging, timing, auth, caching

If you want, I can explain decorators **step-by-step**, **visually**, or show **interview-style questions** or **advanced patterns** (like async decorators).
