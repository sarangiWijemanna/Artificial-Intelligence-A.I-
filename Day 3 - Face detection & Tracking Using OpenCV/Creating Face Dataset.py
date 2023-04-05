import cv2
import os  # For directory operations

folder = "dataset"  # Initializing Folder Name
subFolder = "captured"  # Initializing Sub folder

# Save with specific path
path = os.path.join(folder, subFolder)

# If directory/ folder path is not existed
if not os.path.isdir(path):

    # Make directory/ folder path locally
    os.mkdir(path)

# Initialized weight and height to save image
(width, height) = (100, 100)

# Initialized haar cascade .xml
haar_file = 'haarcascade_frontalface_default.xml'

# Load that algorithm to computer vision
face_cascade = cv2.CascadeClassifier(haar_file)

# Capture webCam image
webcam = cv2.VideoCapture(0)

# Initialized count variable
count = 1

while count < 31:
    print(count)

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

        # Only detect the face not other parts to image
        faceOnly = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(faceOnly, (width, height))

        # Save image in local directory
        cv2.imwrite('%s/%s.png' % (path, count), face_resize)

    count += 1

    # Display Image
    cv2.imshow('Face Detection', image)

    # Escape
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):  # If press 'q', then exist from loop
        break

print("Image Captured Successfully..!")

# Release Camera
webcam.release()

# Close all windows
cv2.destroyAllWindows()
