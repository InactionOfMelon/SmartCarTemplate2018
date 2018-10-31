import paho.mqtt.client as mqtt

# Configuration Begin #

MQTT_BROKER = "mqtt.gycis.me"
MQTT_TOPIC_ID = "inactionofmelon"
MQTT_TOPIC_RCCONTROL = "/smartcar/" + MQTT_TOPIC_ID + "/rccontrol"
MQTT_TOPIC_STATUS = "/smartcar/" + MQTT_TOPIC_ID + "/status"
MQTT_QOS = 1

CLIENT_USERNAME = "smartcar"
CLIENT_PASSWORD = "smartcar"

CAR_DEFAULT_SPEED = -1
CAR_DEFAULT_SPEED_DIFF = -1

# Configuration End #

# Car Control Begin #

def car_stop():
	pass

def car_forward(speed):
	pass

def car_backward(speed):
	pass

def car_left(speed_diff):
	pass


def car_right(speed_diff):
	pass

def car_clockwise():
	pass

def car_anticlockwise():
	pass

# Car Control End #

# MQTT Client Begin #

MQTT_CONNECT_ERROR = ["0: Connection successful", "1: Connection refused - incorrect protocol version", "2: Connection refused - invalid client identifier", "3: Connection refused - server unavailable", "4: Connection refused - bad username or password", "5: Connection refused - not authorised"]

def __str2int(val, default):
	return default if val == '' else int(val)

def mqtt_on_connect(client, userdata, flags, rc):
	client.subscribe(MQTT_TOPIC_RCCONTROL)
	client.subscribe(MQTT_TOPIC_STATUS)
	client.publish(MQTT_TOPIC_STATUS, MQTT_CONNECT_ERROR[rc])

def mqtt_on_message(client,	userdata, msg):
	if msg.topic == MQTT_TOPIC_RCCONTROL:
		if msg.payload[0] == 'f':   # forward
			car_forward(__str2int(msg.payload[7:], CAR_DEFAULT_SPEED))
		elif msg.payload[0] == 's': # stop
			car_stop()
		elif msg.payload[0] == 'b': # backward
			car_backward(__str2int(msg.payload[8:], CAR_DEFAULT_SPEED))
		elif msg.payload[0] == 'l': # left
			car_left(__str2int(msg.payload[4:], CAR_DEFAULT_SPEED_DIFF))
		elif msg.payload[0] == 'r': # right
			car_right(__str2int(msg.payload[4:], CAR_DEFAULT_SPEED_DIFF))
		elif msg.payload[0] == 'c': # clockwise
			car_clockwise()
		elif msg.payload[0] == 'a': # anti-clockwise
			car_anticlockwise()
		elif msg.payload[0] == 'o': # other
			pass
		else:
			print("%s: %s" % (msg.topic, msg.payload))
	else:
		print("%s: %s" % (msg.topic, msg.payload))

client = mqtt.Client()
client.username_pw_set(CLIENT_USERNAME, CLIENT_PASSWORD)
client.on_connect = mqtt_on_connect
client.on_message = mqtt_on_message
client.connect(MQTT_BROKER)
client.loop_forever()

# MQTT Client End #
