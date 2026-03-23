from concurrent.futures import ThreadPoolExecutor
from multithreading import fun
from time import time

def main():
  time1 = time()
  with ThreadPoolExecutor() as executor:
    list = [5, 3, 1]
    results = executor.map(fun, list)

    for result in results:
      print(result)

  time2 = time()

  print(time2 - time1)

main()