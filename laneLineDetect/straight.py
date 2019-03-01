import camera
import car
import time
import detect_new as detect

def straight(error):
	if error < 0:
		car.left_adjustment(-error)
	elif error > 0:
		car.right_adjustment(error)

def work(handler):
	car.set_speed(500)
	#car.forward()
	cnt = 0
	handler.func=straight
	#handler = camera.Handler(straight)
	#time.sleep(1)
	t0 = time.time()
	try:
		cnt=0
		tmp=None
		while True:
			tmp=handler.work_for_point(t0)
			if (tmp!=None):
				break
			handler.work()
			cnt+=1
			pass
		print('Find a point')
		car.stop()
		
		if (cnt>0):
			car.short_backward(0.15)
			car.stop()
			time.sleep(1)
		point=handler.work_for_point(t0)
		
		if point!=None:
			tmp=(float(point+77)**0.5)/34
			car.short_forward(tmp)
			car.stop()
			
	except KeyboardInterrupt:
		car.stop()
		pass
	del handler


if __name__ == '__main__':
	handler=camera.Handler()
	work(handler)