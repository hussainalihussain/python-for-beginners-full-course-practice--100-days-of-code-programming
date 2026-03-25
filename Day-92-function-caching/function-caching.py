import functools
import time

@functools.lru_cache(maxsize=None)
def fx(x):
  time.sleep(3)
  return x * 2

print(fx(2))
print('-> run for 2')

print(fx(4))
print('-> run for 4')

print(fx(6))
print('-> run for 6')

print(fx(8))
print('-> run for 8')

print(fx(2))
print('-> run for 2')

print(fx(6))
print('-> run for 6')

print(fx(81))
print('-> run for 81')

print(fx(28))
print('-> run for 28')
