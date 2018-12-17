import cv2
cap=cv2.VideoCapture(0)
print "camera launched"
ret,frame=cap.read()
cv2.imwrite("camera.jpg",frame)

