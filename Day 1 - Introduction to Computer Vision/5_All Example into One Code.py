import cv2
import imutils  # Resizing Images

image = cv2.imread("Girl.png")  # Read Image
resizeImage = imutils.resize(image, width=105)   # Resize Image

# Smoothing Image
# gaussainBlurImage = cv2.GaussianBlur(resizeImage, (5,5), cv2.BORDER_DEFAULT)

# Convert Color Image To Binary Image
grayImage = cv2.cvtColor(resizeImage, cv2.COLOR_BGR2GRAY)
# threshImage = cv2.threshold(grayImage, 180, 255, cv2.THRESH_BINARY)[1]

# Save Image
cv2.imwrite("5_convertedImage.png", grayImage)

