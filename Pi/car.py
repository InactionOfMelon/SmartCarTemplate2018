import env
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
	x = [110, speed & (0xFF), speed >> 8, 0, 1]
	spi.xfer2(x)

def right_param(speed_diff):
	x = [111, speed & (0xFF), speed >> 8, 0, 1]
	spi.xfer2(x)

def set_pid_param_Kp(Kp):
	x = [112, Kp & (0xFF), Kp >> 8, 0, 1]
	spi.xfer2(x)

def set_pid_param_Ki(Ki):
	x = [113, Ki & (0xFF), Ki >> 8, 0, 1]
	spi.xfer2(x)
	
def set_pid_param_Kd(Kd):
	x = [114, Kd & (0xFF), Kd >> 8, 0, 1]
	spi.xfer2(x)
	
def set_pid_param(Kp, Ki, Kd):
        set_pid_param_Kp(Kp)
        set_pid_param_Ki(Ki)
        set_pid_param_Kd(Kd)
