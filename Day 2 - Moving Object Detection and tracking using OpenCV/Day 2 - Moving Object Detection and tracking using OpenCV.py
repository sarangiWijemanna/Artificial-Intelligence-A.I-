import cv2
import time
import imutils

cam = cv2.VideoCapture(0)
time.sleep(1)

firstFrame = None
movedObjectCount = 0
area = 500

while True:
    _, img = cam.read()
    text = "Normal"
    img = imutils.resize(img, width=500)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gaussianImg
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg)
    threshImg = cv2.threshold(imgDiff, 50, 255, cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg, None, iterations=2)
    cnt = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = imutils.grab_contours(cnt)
    for c in cnt:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        movedObjectCount += 1
        text = "Moving object detected"
    print(f"{text},count={movedObjectCount}")

    cv2.putText(img, f"{text},count={movedObjectCount}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("cameraFeed", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
