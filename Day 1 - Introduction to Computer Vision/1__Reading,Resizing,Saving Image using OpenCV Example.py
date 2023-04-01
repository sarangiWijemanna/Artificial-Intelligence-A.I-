import cv2
import imutils  # Resizing Images

image = cv2.imread("Girl.png")  # Read Image
resizeImage = imutils.resize(image, width=65)   # Resize Image
cv2.imwrite("1_resizedImage.png", resizeImage) # Save Resized Image
