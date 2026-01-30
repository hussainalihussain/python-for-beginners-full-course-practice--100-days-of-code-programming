import time

def timer(func):
  def wrapper():
    start = time.time()
    func()
    end = time.time()

    print("Time taken:", (end - start))
  
  return wrapper

@timer
def sample():
  time.sleep(2)


sample()


@timer
def some_db_work():
  print("Sample of db work is started......")
  print("Db started....")
  time.sleep(2)
  print("Db fetch some data....")
  time.sleep(1)
  print("Everything is done")


print()

some_db_work()