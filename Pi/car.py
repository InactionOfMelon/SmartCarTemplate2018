import env
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=5000

def stop():
	x = [102, 0, 0, 0, 0]
	spi.xfer2(x)

def forward(speed):
	x = [101, 0, 0, 0, 0]
	spi.xfer2(x)

def backward(speed):
	x = [103, 0, 0, 0, 0]
	spi.xfer2(x)

def left(speed_diff):
	x = [104, 0, 0, 0, 0]
	spi.xfer2(x)

def right(speed_diff):
	x = [105, 0, 0, 0, 0]
	spi.xfer2(x)

def clockwise():
	x = [107, 0, 0, 0, 0]
	spi.xfer2(x)

def anticlockwise():
	x = [106, 0, 0, 0, 0]
	spi.xfer2(x)
