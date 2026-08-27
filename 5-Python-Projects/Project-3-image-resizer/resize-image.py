import cv2

image_name = 'tree.jpg'
resizing_image_name = 'tree-resized.jpg'


img = cv2.imread(image_name)
width = img.shape[1]
height = img.shape[0]

scale_percentage = 70

print(f"{width}x{height}")

new_width = int((width * scale_percentage) / 100)
new_height = int((height * scale_percentage) / 100)

new_image = cv2.resize(img, (new_width, new_height))

cv2.imwrite(resizing_image_name, new_image)

cv2.imshow('Image Preview', img)
cv2.imshow('Image Preview', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()