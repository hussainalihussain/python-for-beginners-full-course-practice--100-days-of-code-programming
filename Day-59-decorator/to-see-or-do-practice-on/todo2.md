Love that you want **real-life practice examples** 👍
Here are **practical, industry-style decorator examples** you can actually use and play with. Each one comes with a small task so you can practice.

---

## 1️⃣ Logging user actions (Web / App logging)

### Real life:

Track what functions users are calling (common in APIs & backend services).

### Code:

```python
from functools import wraps
from datetime import datetime

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

```python
@log_action
def create_user(username):
    print(f"User '{username}' created")
```

**Try this:**

```python
create_user("alice")
```

💡 **Practice task:**
Modify the decorator to also log function arguments.

---

## 2️⃣ Authentication check (Very common)

### Real life:

Prevent access to protected resources unless user is logged in.

### Code:

```python
def login_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in"):
            raise PermissionError("Login required")
        return func(user, *args, **kwargs)
    return wrapper
```

```python
@login_required
def view_dashboard(user):
    print(f"Welcome {user['name']}!")
```

```python
user = {"name": "Bob", "logged_in": True}
view_dashboard(user)
```

💡 **Practice task:**
Change it so the decorator prints `"Access denied"` instead of raising an error.

---

## 3️⃣ Measure execution time (Performance monitoring)

### Real life:

Used in debugging slow APIs, ML models, database queries.

### Code:

```python
import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper
```

```python
@measure_time
def slow_task():
    time.sleep(2)
```

**Run:**

```python
slow_task()
```

💡 **Practice task:**
Make it print a warning if execution time > 1 second.

---

## 4️⃣ Retry on failure (Networking / APIs)

### Real life:

Retry failed API calls or database connections.

### Code:

```python
import random
from functools import wraps

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed")
                    if attempt == times:
                        raise
        return wrapper
    return decorator
```

```python
@retry(3)
def unstable_api():
    if random.random() < 0.7:
        raise ValueError("API error")
    print("API call successful")
```

💡 **Practice task:**
Add a `time.sleep(1)` delay between retries.

---

## 5️⃣ Input validation (Data safety)

### Real life:

Validate inputs before saving to DB or processing data.

### Code:

```python
def validate_positive(func):
    def wrapper(amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return func(amount)
    return wrapper
```

```python
@validate_positive
def deposit(amount):
    print(f"Deposited ${amount}")
```

💡 **Practice task:**
Make it work with multiple arguments.

---

## 6️⃣ Caching results (Performance boost)

### Real life:

Avoid recomputing expensive calculations.

### Code:

```python
from functools import wraps

def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(x):
        if x in cache:
            print("Returning cached result")
            return cache[x]
        result = func(x)
        cache[x] = result
        return result

    return wrapper
```

```python
@simple_cache
def square(n):
    print("Computing...")
    return n * n
```

💡 **Practice task:**
Extend cache to support multiple parameters.

---

## 🔥 Mini Challenge (Real Interview-style)

Write a decorator that:

* Counts how many times a function is called
* Prints the count every time

Want me to:

* Review your solution?
* Give **step-by-step hints**?
* Share **common decorator interview traps**?

Just say the word 😄
