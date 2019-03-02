import car
import time

for i in range(20):
	car.set_speed(500)
	car.forward()
	time.sleep(1)

	car.set_speed(500)

	car.backward()
	time.sleep(1)
	car.stop()