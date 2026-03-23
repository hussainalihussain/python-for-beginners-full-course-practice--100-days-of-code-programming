## 🧠 What is Multithreading?

👉 Multiple **workers (threads)** doing work **at the same time**

---

## 🍕 Example: Pizza shop

### ❌ Without multithreading

Only 1 worker:

* takes order
* makes pizza
* delivers

👉 All customers wait 😴

---

### ✅ With multithreading

Many workers:

* Worker 1 → making pizza
* Worker 2 → packing
* Worker 3 → delivery

👉 Work happens **at same time**

---

## 🧩 Python example (simple)

```python
import threading
import time

def work(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

t1 = threading.Thread(target=work, args=("Task 1",))
t2 = threading.Thread(target=work, args=("Task 2",))

t1.start()
t2.start()

t1.join()
t2.join()
```

👉 Both tasks run together

---

## 🚗 Example: Car wash station

* 1 person → washing
* 1 person → drying

```python
import threading
import time

def wash():
    print("Washing car")
    time.sleep(3)
    print("Wash done")

def dry():
    print("Drying car")
    time.sleep(2)
    print("Dry done")

t1 = threading.Thread(target=wash)
t2 = threading.Thread(target=dry)

t1.start()
t2.start()

t1.join()
t2.join()
```

👉 No waiting → faster

---

## 📦 Example: Packing orders

```python
import threading
import time

def pack(order):
    print(f"Packing {order}")
    time.sleep(1)
    print(f"{order} packed")

threads = []

for i in range(5):
    t = threading.Thread(target=pack, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

👉 Many orders packed at same time

---

## ⚠️ Important truth (very important)

👉 Python threads are **not fully parallel** for heavy work
(because of something called GIL)

---

## 🧠 When to use multithreading?

Use when:

* waiting (files, network, I/O)
* doing many small tasks

---

## ❌ When NOT to use

Don’t use for:

* heavy calculations
  👉 use multiprocessing instead

---

## 🔥 asyncio vs threading (simple)

| Thing    | asyncio                  | threading            |
| -------- | ------------------------ | -------------------- |
| Style    | 1 worker switching tasks | many workers         |
| Good for | waiting tasks            | small parallel tasks |
| Control  | more structured          | easier start         |

---

## 🧠 One-line understanding

👉 Multithreading = “many workers working together”
