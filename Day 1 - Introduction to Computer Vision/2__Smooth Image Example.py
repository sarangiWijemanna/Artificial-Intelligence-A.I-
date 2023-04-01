import cv2  # For Read & Write Images

image = cv2.imread("Girl.png")  # Read Image

gaussainBlurImage = cv2.GaussianBlur(image, (5,5), cv2.BORDER_DEFAULT)
cv2.imwrite("2_gaussainBluredImage.png", gaussainBlurImage)
