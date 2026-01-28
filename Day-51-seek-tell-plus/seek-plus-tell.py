with open('file.txt') as f:
  print(f"content of the file: {f.read()}")

with open('file.txt', 'r') as f:
  f.seek(4)

  whichLine = f.tell()

  print(f"We are at line#{whichLine}")

  print(f"We getting from the file: {f.read()}")