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

# MQTT Client Begin #

MQTT_CONNECT_ERROR = ["0: Connection successful", "1: Connection refused - incorrect protocol version", "2: Connection refused - invalid client identifier", "3: Connection refused - server unavailable", "4: Connection refused - bad username or password", "5: Connection refused - not authorised"]

def __str2int(val, default):
	return default if val == '' else int(val)

def mqtt_on_connect(client, userdata, flags, rc):
#	client.subscribe(MQTT_TOPIC_RCCONTROL)
	client.subscribe(MQTT_TOPIC_STATUS)
#	print("rc %s" % (MQTT_CONNECT_ERROR[rc]))

def mqtt_on_message(client,	userdata, msg):
#	print("%s (%d): %s" % (msg.topic, msg.qos, msg.payload))
	pass

client = mqtt.Client()
client.username_pw_set(CLIENT_USERNAME, CLIENT_PASSWORD)
client.on_connect = mqtt_on_connect
client.on_message = mqtt_on_message
client.connect(MQTT_BROKER)
client.loop_start()

while True:
	text = raw_input("text to send: ")
	client.publish(MQTT_TOPIC_RCCONTROL, text)

# MQTT Client End #
