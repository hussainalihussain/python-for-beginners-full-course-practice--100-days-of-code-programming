import os

directory = 'directory'



print(f"Clear the clutter from {directory} by organizing images with number...")

i = 1

for image in os.listdir(directory):
    if not image.endswith('.jpg'):
        continue

    print(f"Ranaming {directory}/{image} -> {directory}/{i}.jpg")

    os.rename(f"{directory}/{image}", f"{directory}/{i}.jpg")
    i = i+1
