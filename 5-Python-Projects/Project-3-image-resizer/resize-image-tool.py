import cv2

image_path = input("Path of the image to resize (with extension):\n")


image = cv2.imread(image_path)

width = image.shape[1]
height = image.shape[0]

print(f"The current size: {width}x{height}")

print()
action = input("Enter an action (1-2):\n1. Just Preview\n2. Resize\n21. Resize with Scale (%age)\n")


def input_width():
  new_width = int(input("New Width (Number only):\n"))

  return new_width


def input_height():
  new_height = int(input("New Height (Number only):\n"))

  return new_height


def input_filename():
  return input("New Resize Image Name (with extension, 'r' to replace):\n")


def need_replace(str):
  return str == 'r'


def input_scale():
  return int(input('Scale in percentag (only number):\n'))


def resize_image(scale):
  print()

  if scale:
    scale = input_scale()
    new_width = int((scale * image.shape[1]) / 100)
    new_height = int((scale * image.shape[0]) / 100)
  else:
    new_width = input_width()
    new_height = input_height()

  new_image_filename = input_filename()

  if need_replace(new_image_filename):
    new_image_filename = image_path

  print()
  print(f"Resizing to {new_width}x{new_height}")

  new_image = cv2.resize(image, (new_width, new_height))
  cv2.imwrite(new_image_filename, new_image)
  

if action == '1':
  cv2.imshow("Preview Image", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
elif action == '2':
  resize_image(False)
elif action == '21':
  resize_image(True)
