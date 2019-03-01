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
		while handler.work(True, t0)[0]!=True:
			cnt+=1
			pass
		print('Find a point')
		car.stop()
		if (cnt>2):
			car.short_backward(0.15)
			car.stop()
			time.sleep(1)
		status, point=handler.work(True, t0)
		
		if status==True:
			tmp=(float(point+115)**0.5)/30
			print('forward',tmp)
			car.stop()
			car.short_forward(tmp)
			car.stop()
	except KeyboardInterrupt:
		car.stop()
		pass
	del handler
