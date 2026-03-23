from concurrent.futures import ThreadPoolExecutor
from multithreading import fun
from time import time

def main():
  time1 = time()
  
  with ThreadPoolExecutor() as executor:
    executor.submit(fun, 5)
    executor.submit(fun, 3)
    executor.submit(fun, 1)
  
  time2 = time()

  print(time2 - time1)

main()
