# 🧠 Same problem, 3 ways

👉 Task: do 3 jobs that each take 2 seconds

---

# 1️⃣ Normal (no async, no threads)

```python
import time

def work(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} done")

start = time.time()

work("A")
work("B")
work("C")

print("Total:", time.time() - start)
```

👉 Output time ≈ **6 sec**
👉 One by one (slow)

---

# 2️⃣ Multithreading

```python
import threading
import time

def work(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} done")

start = time.time()

t1 = threading.Thread(target=work, args=("A",))
t2 = threading.Thread(target=work, args=("B",))
t3 = threading.Thread(target=work, args=("C",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Total:", time.time() - start)
```

👉 Output time ≈ **2 sec**
👉 Works well because of **waiting (sleep)**

---

# 3️⃣ asyncio

```python
import asyncio
import time

async def work(name):
    print(f"{name} start")
    await asyncio.sleep(2)
    print(f"{name} done")

async def main():
    await asyncio.gather(
        work("A"),
        work("B"),
        work("C")
    )

start = time.time()

asyncio.run(main())

print("Total:", time.time() - start)
```

👉 Output time ≈ **2 sec**
👉 Same benefit as threading, but cleaner

---

# 4️⃣ Multiprocessing (REAL parallel)

```python
from multiprocessing import Process
import time

def work(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} done")

start = time.time()

p1 = Process(target=work, args=("A",))
p2 = Process(target=work, args=("B",))
p3 = Process(target=work, args=("C",))

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

print("Total:", time.time() - start)
```

👉 Output time ≈ **2 sec**
👉 Truly parallel (different CPUs)

---

# 🔥 Final understanding (very important)

| Type            | Real-life meaning        | Best for            |
| --------------- | ------------------------ | ------------------- |
| Normal          | 1 worker                 | simple tasks        |
| Threading       | many workers, 1 brain    | I/O tasks           |
| asyncio         | 1 smart worker switching | I/O tasks (cleaner) |
| Multiprocessing | many brains              | heavy CPU           |

---

# 🧠 Super simple summary

* `asyncio` → smart waiting
* `threading` → many workers (but GIL)
* `multiprocessing` → real power 💪

---

# 🚀 For YOU (based on your work)

Use:

* Scraping → **asyncio ✅**
* Downloads → **asyncio ✅**
* Heavy processing → **multiprocessing ✅**
