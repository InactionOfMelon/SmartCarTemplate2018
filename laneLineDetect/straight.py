import camera
import car
import time

def straight(error):

	if error < 0:
		car.left_adjustment(-error)
	elif error > 0:
		car.right_adjustment(error)
		
car.set_speed(450)
#car.forward()
cnt = 0
handler = camera.Handler(straight)
time.sleep(1)
try:
	while True:
		#time.sleep(0)
		handler.work()
except KeyboardInterrupt:
	car.stop()
	del handler