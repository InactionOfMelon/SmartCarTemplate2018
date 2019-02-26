import camera
import car
import time

def adjustment(error):
	if error<200 and error>-200:
		return 1
	else:
		car.self_adjustment(error)
		return 0


cnt = 0
great = 0
handler = camera.Handler(adjustment)
try:
	while True:
		time.sleep(0)
		tmp=handler.work()
		if tmp==1:
			great+=1
		else:
			great=0
		if great>2:
			break
except KeyboardInterrupt:
	car.stop()
	del handler