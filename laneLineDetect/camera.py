import cv2
import time
import detect_new as detect
import numpy as np
import car
import random

cap=cv2.VideoCapture(0)
print "camera launched"

def saveImageTo(img, fileName):
    cv2.imwrite(fileName, img)
    print(fileName)

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

def work():
	ret,frame=cap.read()
	#frame=cv2.imread('5.jpg')
	#ret=True
	h,w=frame.shape[:2]
	if not ret:
		print "capture error"
                raise Exception('Car stopped')
	#cv2.imwrite("camera.jpg",frame)
	
	error,ret=detect.detect_lines(frame)

	if not ret:
		cv2.imwrite("camera.jpg",frame)
		++cnt
		if cnt > 10:
			raise Exception('Car stopped')
                return
	else:
		cnt = 0
	print error
        #car.self_adjustment(error)
        if error > 1000 or error< -1000:
            saveImageTo(frame, "figure" + str(random.randint(0, 10000)) + '.jpg')
            exit()
	if error < 0:
		car.left_adjustment(-error)
	elif error > 0:
		car.right_adjustment(error)

	#break

	#time.sleep(1)
	
	
car.set_speed(450)
car.forward()
cnt = 0
while True:
	try:
		work()
	except KeyboardInterrupt:
		car.stop()
		exit()

