import cv2

img = cv2.imread('tree.jpg')
cv2.imshow('Image Preview', img)
cv2.waitKey(0)
cv2.destroyAllWindows()