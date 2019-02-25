import threading
import time

lock = threading.Lock()
a = 0
def f():
	global a
	while True:
		lock.acquire()
		a ^= 1
		lock.release()
threading.Thread(target=f, args=()).start()
for i in range(10):
	lock.acquire()
	print(a)
	lock.release()
	time.sleep(1)
