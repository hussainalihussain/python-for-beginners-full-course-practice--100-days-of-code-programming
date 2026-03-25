def generator():
  for i in range(5000000):
    yield i

gen = generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# for gen_item in gen:
#   print(gen_item)

iterator = 0

for gen_item in gen:
  if iterator > 100:
    break

  print(gen_item)
  iterator += 1