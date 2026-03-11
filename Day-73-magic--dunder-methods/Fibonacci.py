# Caching / Memoization
# ✔ Encapsulates cache cleanly.

class Fibonacci:
  def __init__(self):
    self.cache = {}
  
  def __call__(self, n):
    if n in self.cache:
      return self.cache[n]

    if n <= 1:
      return n
    
    self.cache[n] = self(n-1) + self(n-2)

    return self.cache[n]