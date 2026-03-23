import requests

def downloadFile(url, name):
  print(f"Started downloading of {name}")
  response = requests.get(url)
  open(f"files/{name}.jpg", "wb").write(response.content)
  print(f"Finished downloading of {name}")


def main():
  url = "https://picsum.photos/2000/3000"

  for i in range(5):
    downloadFile(url, i+1)

if __name__ == '__main__':
  main()