import camera
import car
import time

def adjustment(error):
	if error<20 and error>-20:
		return True
	else:
		car.self_adjustment(error)
		return False

def work(handler):
	cnt = 0
	great = 0
	handler.func=adjustment
	#handler = camera.Handler(adjustment)
	#time.sleep(1)
	try:
		while True:
			#time.sleep(0)
			point,error=handler.work()
			if adjustment(error):
				great+=1
			else:
				great=0
			if great>2:
				break
	except KeyboardInterrupt:
		pass
	del handler

if __name__ == '__main__':
	handler=camera.Handler()
	work(handler)