import camera
import car
import time

def adjustment(error):
	if error<100 and error>-100:
		return 1
	else:
		car.self_adjustment(error)
		return 0


cnt = 0
great = 0
handler = camera.Handler(adjustment)
time.sleep(1)
try:
	while True:
		#time.sleep(0)
		_, tmp=handler.work()
		if tmp==1:
			great+=1
		else:
			great=0
		if great>2:
			del handler
			break
except KeyboardInterrupt:
	del handler
