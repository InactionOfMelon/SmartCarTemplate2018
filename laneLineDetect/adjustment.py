import cv2
import time
import detect_new as detect
import numpy as np
import car
import random
import threading


class ipcamCapture:
    def __init__(self, URL):
        self.Frame = []
        self.status = False
        self.isstop = False
		
        self.capture = cv2.VideoCapture(0)

    def start(self):
        print('ipcam started!')
        threading.Thread(target=self.queryframe, args=()).start()

    def stop(self):
        self.isstop = True
        print('ipcam stopped!')
   
    def getframe(self):
        return self.Frame
        
    def queryframe(self):
        while (not self.isstop):
            self.status, self.Frame = self.capture.read()
        
        self.capture.release()

		
		
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
	frame=ipcam.getframe()
	#frame=cv2.imread('5.jpg')
	#ret=True
	h,w=frame.shape[:2]
	#if not ret:
	#	print "capture error"
	#	raise Exception('Car stopped')
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
	
	car.self_adjustment(error)
	if error > 0 or error< -0:
		saveImageTo(frame, "figure" + str(random.randint(0, 10000)) + '.jpg')
		#exit()
	
	if error<200 and error>-200:
		return 0
	else:
		return 0
	#if error < 0:
	#	car.left_adjustment(-error)
	#elif error > 0:
	#	car.right_adjustment(error)

	#break

	
	
cnt = 0
great = 0
ipcam = ipcamCapture(0)
ipcam.start()
time.sleep(1)
while True:
	try:
		tmp=work()
		if tmp==1:
			great+=1
		else:
			great=0
			
		if great>2:
			break
			time.sleep(2)
	except KeyboardInterrupt:
		car.stop()
		exit()


ipcam.stop()