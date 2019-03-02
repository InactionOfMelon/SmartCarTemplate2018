import camera
import car
import time
import detect_new as detect

def straight(error):
	if error < 0:
		car.left_adjustment(-error)
	elif error > 0:
		car.right_adjustment(error)

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
			if cnt>0:
				car.set_speed(400)
			else:
				car.set_speed(400)
			
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
		print(point)
		
		if point!=None:
			car.set_speed(500)
			tmp=(float(point+65)**0.5)/36
			car.short_forward(tmp)
			car.stop()
			
	except KeyboardInterrupt:
		car.stop()
		pass
	del handler


if __name__ == '__main__':
	handler=camera.Handler()
	work(handler,0)