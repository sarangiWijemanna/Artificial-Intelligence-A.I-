import cv2  # For Read & Write Images

# Read Image
image = cv2.imread("Girl.png")

# Convert Color Image To Binary Image
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshImage = cv2.threshold(grayImage, 180, 255, cv2.THRESH_BINARY)[1]

# Save Image
cv2.imwrite("3_convertedImage.png", threshImage)
