import cv2
import time
import detect_new as detect
import numpy as np
import car
import random
import threading


class ipcamCapture:
	TIMEOUT = 2
	def __init__(self, URL):
		self.Frame = None
		self.status = False
		self.isstop = False
		self.lock = threading.Lock()
		self.capture = cv2.VideoCapture(0)
		#self.thread = threading.Thread(target=self.queryframe, args=())

	def start(self):
		print('ipcam started!')
		self.thread.setDaemon(True)
		self.thread.start()

	def stop(self):
		self.isstop = True
		print('ipcam stopped!')
		time.sleep(0)
   
	def getframe(self):
		for i in range(4):
			self.status, frame = self.capture.read()
		t = 0
		while t <= 0.035:
			t1 = time.time()
			self.status, frame = self.capture.read()
			t2 = time.time()
			t = t2 - t1
		return frame
		##self.lock.acquire()#timeout = ipcamCapture.TIMEOUT)
		#frame = self.Frame
		##self.lock.release()
		#return frame
		
	def queryframe(self):
		while (not self.isstop):
			#self.lock.acquire()#timeout = ipcamCapture.TIMEOUT)
			self.status, self.Frame = self.capture.read()
			#self.lock.release()
			time.sleep(0)
		self.capture.release()
		#raise KeyboardInterrupt()

		
		
print('camera launched')

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

class Handler:
	def __init__(self):
		self.ipcam = ipcamCapture(0)
		#self.ipcam.start()
	def __del__(self):
		#self.ipcam.stop()
		pass
	def work_for_point(self, t0 = 0.0):
		print('point:',tmp)
		return tmp
		
	def work(self):
		frame=self.ipcam.getframe()
		saveImageTo(frame, "figure" + str(random.randint(0, 999)) + '.jpg')
		ret=self.ipcam.status
		if frame is None:
			print('None')
			return True, None
		#frame=cv2.imread('5.jpg')
		#ret=True
		h,w=frame.shape[:2]
		
		
		error,ret,leftLine,rightLine=detect.detect_lines(frame)
			
		get_point=detect.detect_point(frame, 0,[leftLine,rightLine])
		
		
		print(error)
		
		#if error > 0 or error< -0:
			#saveImageTo(frame, "figure" + str(random.randint(0, 99)) + '.jpg')
			#exit()
		return get_point,error

		#break

