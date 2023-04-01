import cv2

videoCapturedImage = cv2.VideoCapture(0)

while True:
    _, image = videoCapturedImage.read()  # Read Frame from Camera
    cv2.imshow("Video Stream", image)  # Show Video Image

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):  # If press 'q', then exist from loop
        break

videoCapturedImage.release() # Realized Cameras
cv2.destroyAllWindows()  # Frame/ all windows Closed
