import os
import car
import straight
import camera
import adjustment
import time

def work(handler):
	
	for i in range(4):
		time.sleep(0.1)
		adjustment.work(handler)
		print(i," adjustment")
		
		time.sleep(0.1)
		straight.work(handler)
		print(i," straight")
		
		time.sleep(0.1)
		car.left_turn(70)
		print(i," turn")

handler = camera.Handler()

if __name__ == '__main__':
	try:
		work(handler)
		pass
	except :
		car.stop()