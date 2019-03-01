import camera
import car
import time


def cover_point():
	status, point=handler.work(True, t0)
	
	if status==False:
		tmp=(float(point)**0.5)/150
		car.stop()
		car.short_forward(tmp)