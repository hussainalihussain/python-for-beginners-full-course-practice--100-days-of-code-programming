import requests
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

def downloadFile(url, name):
  print(f"Started downloading of {name}")
  response = requests.get(url)
  open(f"files/{name}.jpg", "wb").write(response.content)
  print(f"Finished downloading of {name}")

url = "https://picsum.photos/2000/3000"
url = "https://picsum.photos/200/300"

def main():
  processes = []

  for i in range(5):
    p = multiprocessing.Process(target=downloadFile, args=(url, i+1,))
    processes.append(p)
    p.start()
  
  for process in processes:
    process.join()

def main_using_concurrent_dot_future():
  with ProcessPoolExecutor() as executor:
    for i in range(5):
      executor.submit(downloadFile, url, i+1)

def main_using_concurrent_dot_future_with_iterator():
  with ProcessPoolExecutor() as executor:
    # Note: _ = placeholder as we are not using any variable so then we can use _ (as a placeholder), but
    # if we need (or even if don't needed) then we can do it:
    # urls = [url for i in range(5)] # but if not used then it is not good idea to used (as some of the
    # IDEs saying "variable unused" also it is not a good practice)
    #
    # 👉
    # _ = underscore variable = throwaway variable
    urls = [url for _ in range(5)]
    names = [i+1 for i in range(5)]

    results = executor.map(downloadFile, urls, names)

    for result in results:
      print(result)

if __name__ == '__main__':
  # main()
  # main_using_concurrent_dot_future()
  main_using_concurrent_dot_future_with_iterator()