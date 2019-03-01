import car
import time

car.set_speed(500)
car.forward()
time.sleep(1)

car.set_speed(0)
car.forward()
car.set_speed(500)


car.backward()
time.sleep(1)
car.stop()