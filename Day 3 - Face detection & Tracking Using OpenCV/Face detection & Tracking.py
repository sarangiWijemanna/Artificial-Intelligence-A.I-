import cv2

# Initialized haar cascade .xml
haar_file = 'haarcascade_frontalface_default.xml'

# Load that algorithm to computer vision
face_cascade = cv2.CascadeClassifier(haar_file)

# Capture webCam image
webcam = cv2.VideoCapture(0)

while True:

    # Read Camera Input
    (_, image) = webcam.read()

    # Convert image to Gray Image

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Pass haar_cascade algorithm to gray Image
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    # Face gives x,y,w,h coordinated on face
    for (x, y, w, h) in faces:

        # Now draw rectangle around the face.
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display Image
    cv2.imshow('FaceDetection', image)

    # Escape
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):  # If press 'q', then exist from loop
        break

# Release Camera
webcam.release()

# Close all windows
cv2.destroyAllWindows()
