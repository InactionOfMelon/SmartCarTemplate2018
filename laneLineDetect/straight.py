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
	t0 = time.time()
	
	leftLine = None
	rightLine = None
	
	try:
		cnt=0
		tmp=None
		last_point=-1
		while True:
			if cnt>1:
				car.set_speed(400)
			else:
				car.set_speed(600)
			point,error,leftLine,rightLine=handler.work(leftLine,rightLine,Number)
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
			pass
		print('Find a point')
		car.stop()
		
		if (cnt>0):
			car.short_backward(0.7)
			car.stop()
			time.sleep(1)
		point,error=handler.work()
		
		if point!=None:
			car.set_speed(500)
			tmp=(float(point+70)**0.5)/36
			car.short_forward(tmp)
			car.stop()
			
	except KeyboardInterrupt:
		car.stop()
		pass
	del handler


if __name__ == '__main__':
	handler=camera.Handler()
	work(handler,0)