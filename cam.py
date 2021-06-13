import cv2

url = 'http://192.168.1.112:8080/video' #sends video format
cap = cv2.VideoCapture(url)
cap.set(15, 0.25)

while(True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('camera',cv2.resize(frame,(1280,720)))
    q = cv2.waitKey(1) #puts a delay in processing in 'ms'

    if q == ord("q"):
        break
cv2.destroyAllWindows()
