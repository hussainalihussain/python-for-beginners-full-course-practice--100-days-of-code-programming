# Example: Timing Decorator
# ✔ Real-world use:
#   Logging
#   Caching
#   Authorization
#   Rate limiting

import time 

class Timer:
  def __init__(self, func):
    self.func = func
  
  def __call__(self, *args, **kwargs):
    start = time.time()
    result = self.func(*args, **kwargs)
    end = time.time()
    print(f"Execution time: {end - start}")

    return result