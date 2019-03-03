import camera
import car
import time
import detect_new as detect

def straight(error):
	if error < 0:
		car.left_adjustment(int(-error))
	elif error > 0:
		car.right_adjustment(int(error))

def work(handler, Number):
	#car.forward()
	cnt = 0
	handler.func=straight
	#handler = camera.Handler(straight)
	#time.sleep(1)
	
	
	leftLine = None
	rightLine = None
	
	try:
		cnt=0
		tmp=None
		last_point=-1
		while True:
			t0 = time.time()
			if cnt == 0:
				car.set_speed(550)
			elif cnt == 1:
				car.set_speed(500)
			else:
				car.set_speed(430)
			tmp = last_point
			if Number > 0:
				tmp=1e9
			point,error,leftLine,rightLine=handler.work(leftLine,rightLine,tmp)
			if point != None:
				if point > last_point:
					Number-=1
				last_point=point
			else:
				last_point=-1
			print('********',point,Number)
			if Number < 0:
				break
				
			straight(error)
			cnt+=1
			
			print(time.time()-t0)
			pass
		print('Find a point')
		print(time.time()-t0)
		car.stop()
		
		if (cnt>0):
			#time.sleep(1)
			#car.short_backward(0.75)
			car.stop()
			time.sleep(2)
		point,error,leftLine,rightLine=handler.work(leftLine,rightLine,0)
		print('********',point)
		
		if point!=None:
			car.set_speed(500)
			if (point < 250):
				tmp=(float(point+173)**0.5)/36.5
			else:
				tmp=float(point-290)/470+0.613
			car.short_forward(tmp)
			car.stop()
			time.sleep(0.75)
			
	except KeyboardInterrupt:
		car.stop()
		pass
	del handler


if __name__ == '__main__':
	handler=camera.Handler()
	work(handler,0)