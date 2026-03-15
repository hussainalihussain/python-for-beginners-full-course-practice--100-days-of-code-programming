import time

def whileLoop():
    i = 0

    while i < 5000:
        print(i)
        i = i + 1

def forLoop():
    for i in range(5000):
        print(i)


init1 = time.time()
whileLoop()
end1 = time.time() - init1

init2 = time.time()
forLoop()
end2 = time.time() - init2

print(f"Time taken by while loop {end1}")
print(f"Time taken by for loop {end2}")