import camera
import car
import time
import detect_new as detect

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
	while handler.work(True)[0]:
		pass
except KeyboardInterrupt:
	pass
car.stop()
del handler
