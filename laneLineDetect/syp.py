import os
import car
import straight
import camera
import adjustment
import time

def work():
	handler = camera.Handler()
	
	for i in range(4):
		time.sleep(1)
		adjustment.work(handler)
		print(i," adjustment")
		
		time.sleep(1)
		straight.work(handler)
		print(i," straight")
	
		time.sleep(1)
		car.left_turn(60)
		print(i," turn")

try:
	work()
	pass
except :
	car.stop()