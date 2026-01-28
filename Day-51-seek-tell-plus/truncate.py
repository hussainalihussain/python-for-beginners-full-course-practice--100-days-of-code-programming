with open('my-file.txt', 'w') as f:
  f.write('123456789')
  f.truncate(3)

with open('my-file.txt') as f:
  print(f"After truncation the content: {f.read()}")