import env
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=500

def forward():
	x = [101, 0, 0, 0, 0]
	spi.xfer2(x)

def stop():
	x = [102, 0, 0, 0, 0]
	spi.xfer2(x)

def backward():
	x = [103, 0, 0, 0, 0]
	spi.xfer2(x)

def left():
	x = [104, 0, 0, 0, 0]
	spi.xfer2(x)

def right():
	x = [105, 0, 0, 0, 0]
	spi.xfer2(x)

def anticlockwise():
	x = [106, 0, 0, 0, 0]
	spi.xfer2(x)

def clockwise():
	x = [107, 0, 0, 0, 0]
	spi.xfer2(x)

def forward_param(speed):
	x = [108, speed & (0xFF), speed >> 8, 0, 0]
	spi.xfer2(x)

def backward_param(speed):
	x = [109, speed & (0xFF), speed >> 8, 0, 0]
	spi.xfer2(x)

def left_param(speed_diff):
	x = [110, speed & (0xFF), speed >> 8, 0, 0]
	spi.xfer2(x)

def right_param(speed_diff):
	x = [111, speed & (0xFF), speed >> 8, 0, 0]
	spi.xfer2(x)
