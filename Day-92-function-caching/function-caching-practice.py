import functools
import time

@functools.lru_cache(maxsize=None)
def fibonacci(n):
  time.sleep(1)

  if n < 2:
    return 2

  return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci of 3 =", fibonacci(3))
print("Fibonacci of 15 =", fibonacci(15))
print("Fibonacci of 12 =", fibonacci(12))
print("Fibonacci of 19 =", fibonacci(19))
print("Fibonacci of 12 =", fibonacci(12))
print("Fibonacci of 19 =", fibonacci(19))
print("Fibonacci of 3 =", fibonacci(3))
print("Fibonacci of 15 =", fibonacci(15))
print("Fibonacci of 22 =", fibonacci(22))
print("Fibonacci of 21 =", fibonacci(21))