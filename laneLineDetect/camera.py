import cv2
import time
import detect
import numpy as np

cap=cv2.VideoCapture(0)
print "camera launched"

def dist(x,y,rho,theta):
    a,b = np.cos(theta),np.sin(theta)
    x0,y0 = a*rho,b*rho
    x1,y1 = (x0 + 100*(-b)),(y0 + 100*(a))
    x2,y2 = (x0 - 100*(-b)),(y0 - 100*(a))
    print x1,y1,x2,y2
    array_longi  = np.array([x2-x1, y2-y1])
    array_trans = np.array([x-x1, y-y1])
    array_temp = (float(array_trans.dot(array_longi)) / array_longi.dot(array_longi))
    array_temp = array_longi.dot(array_temp)
    distance   = np.sqrt((array_trans - array_temp).dot(array_trans - array_temp))
    return distance

while True:
    ret,frame=cap.read()
    h,w=frame.shape[:2]
    if not ret:
        print "capture error"
        break
    #cv2.imwrite("camera.jpg",frame)

    lines=detect.detect_lines(frame)
    if lines[0,0,0]>lines[1,0,0]:
        lines[0],lines[1]=lines[1],lines[0]
	print 'lines:'
    print lines

    point=detect.detect_point(frame)
    print 'point:', point

    distLeft=dist(w/2,h,lines[0,0,0],lines[0,0,1])
    distRight=dist(w/2,h,lines[1,0,0],lines[1,0,1])
    
    #time.sleep(1)

