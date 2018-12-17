import cv2
import time
import detect_new as detect
import numpy as np
import car

cap=cv2.VideoCapture(0)
print "camera launched"

def dist(x,y,rho,theta):
	a,b = np.cos(theta),np.sin(theta)
	x0,y0 = a*rho,b*rho
	x1,y1 = (x0 + 100*(-b)),(y0 + 100*(a))
	x2,y2 = (x0 - 100*(-b)),(y0 - 100*(a))
	#print x1,y1,x2,y2
	array_longi  = np.array([x2-x1, y2-y1])
	array_trans = np.array([x-x1, y-y1])
	array_temp = (float(array_trans.dot(array_longi)) / array_longi.dot(array_longi))
	array_temp = array_longi.dot(array_temp)
	distance   = np.sqrt((array_trans - array_temp).dot(array_trans - array_temp))
	return distance

car.set_speed(600)
car.forward()
cnt = 0
while True:
	ret,frame=cap.read()
	#frame=cv2.imread('5.jpg')
	#ret=True
	h,w=frame.shape[:2]
	if not ret:
		print "capture error"
		break
	#cv2.imwrite("camera.jpg",frame)

	error,ret=detect.detect_lines(frame)
	if not ret:
		cv2.imwrite("camera.jpg",frame)
		++cnt
		if cnt > 10:
			break
	else:
		cnt = 0
	print error
	if error < 0:
		car.left_adjustment(-error)
	elif error > 0:
		car.right_adjustment(error)

	#break

	#time.sleep(1)

