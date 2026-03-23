import threading
from time import sleep, time

def fun(seconds):
  print(f"Sleeping for {seconds} seconds")
  sleep(seconds)
  print(f"Task completed after {seconds} seconds")
  
  return seconds

def main():
  # Normal Way
  # time1 = time()

  # fun(5)
  # fun(3)
  # fun(1)
  # time2 = time()

  # print(time2 - time1)


  # Using threading
  time1 = time()

  t1 = threading.Thread(target=fun, args=[5])
  t2 = threading.Thread(target=fun, args=[3])
  t3 = threading.Thread(target=fun, args=[1])

  t1.start()
  t2.start()
  t3.start()

  # to get the accurate time we need to wait for threads to complete (by using join)
  t1.join()
  t2.join()
  t3.join()

  time2 = time()

  print(time2 - time1)


if __name__ == '__main__':
  main()