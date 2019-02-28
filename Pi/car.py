#import env
import time
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=500

def set_speed(speed):
	x = [1, speed & (0xFF), speed >> 8, 0, 1]
	spi.xfer2(x)

"on the left of the road, need turn right"
def right_adjustment(error):
	x = [2, error & (0xFF), error >> 8, 0, 1]
	spi.xfer2(x)

"on the right of the road, need turn left"
def left_adjustment(error):
	x = [3, error & (0xFF), error >> 8, 0, 1]
	spi.xfer2(x)
	
def forward():
	x = [101, 0, 0, 0, 1]
	spi.xfer2(x)

def stop():
	x = [102, 0, 0, 0, 1]
	spi.xfer2(x)

def backward():
	x = [103, 0, 0, 0, 1]
	spi.xfer2(x)

def left():
	x = [104, 0, 0, 0, 1]
	spi.xfer2(x)

def right():
	x = [105, 0, 0, 0, 1]
	spi.xfer2(x)

def anticlockwise():
	x = [106, 0, 0, 0, 1]
	spi.xfer2(x)

def clockwise():
	x = [107, 0, 0, 0, 1]
	spi.xfer2(x)

def forward_param(speed):
	x = [108, speed & (0xFF), speed >> 8, 0, 1]
	spi.xfer2(x)

def backward_param(speed):
	x = [109, speed & (0xFF), speed >> 8, 0, 1]
	spi.xfer2(x)

def left_param(speed_diff):
	x = [110, speed_diff & (0xFF), speed_diff >> 8, 0, 1]
	spi.xfer2(x)

def right_param(speed_diff):
	x = [111, speed_diff & (0xFF), speed_diff >> 8, 0, 1]
	spi.xfer2(x)

def set_pid_param_Kp(f_Kp):
	Kp=(int)(f_Kp*256)
	x = [112, Kp & (0xFF), Kp >> 8, 0, 1]
	spi.xfer2(x)

def set_pid_param_Ki(f_Ki):
	Ki=(int)(f_Ki*256)
	x = [113, Ki & (0xFF), Ki >> 8, 0, 1]
	spi.xfer2(x)
	
def set_pid_param_Kd(f_Kd):
	Kd=(int)(f_Kd*256)
	x = [114, Kd & (0xFF), Kd >> 8, 0, 1]
	spi.xfer2(x)
	
def set_pid_param(Kp, Ki, Kd):
	set_pid_param_Kp(Kp)
	set_pid_param_Ki(Ki)
	set_pid_param_Kd(Kd)

def pid_init():
	x = [115, 0, 0, 0, 1]
	spi.xfer2(x)
	
def left_turn(deg):
	stop()
	set_speed(1000)
	anticlockwise()
	time.sleep(float(deg)/100)
	stop()

def right_turn(deg):
	stop()
	set_speed(1000)
	clockwise()
	time.sleep(float(deg)/100)
	stop()
	
def self_adjustment(error):
	set_speed(1000)
	if error > 0:
		right_turn(4)
	if error < 0:
		left_turn(4)
		
def set_pulse_single(MOTOR, Dir, Pulse):
	x = [200+MOTOR+Dir*10, Pulse & (0xFF), Pulse >> 8, 0, 1]
	spi.xfer2(x)

def set_min_speed(state):
	x = [220, state, 0, 0, 1]
	spi.xfer2(x)

def set_speed_up(rate):
	x = [221, rate, 0, 0, 1]
	spi.xfer2(x)
	
def set_go_back(dir):
	x = [222, dir, 0, 0, 1]
	spi.xfer2(x)