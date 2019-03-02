import time
import paho.mqtt.client as mqtt
import env
import main

def __str2int(val, default):
	return default if val == '' else int(val)

def mqtt_on_connect(client, userdata, flags, rc):
	client.subscribe(env.MQTT_TOPIC_TASK)
	client.subscribe(env.MQTT_TOPIC_CAMMAND)
	__mqtt_report(client, env.MQTT_CONNECT_ERROR[rc])
	if rc == 0:
		client.not_connected = False
	else:
		__mqtt_report(client, 'reconnecting...')

starting_point = 0
finishing_point = 0
def task_dealer(msg):
	global starting_point
	global finishing_point
	starting_point = msg[0]
	finishing_point = msg[1]
	
def command_dealer(msg):
	if(msg[0] == 0x00) main.work(starting_point, finishing_point)
	
def mqtt_on_message(client, userdata, msg):
	if msg.topic == env.MQTT_TOPIC_TASK:
		task_dealer(msg)
	elif msg.topic == env.MQTT_TOPIC_CAMMAND:
		command_dealer(msg)
	print("%s: %s" % (msg.topic, msg.payload))

mqtt.Client.not_connected = True
client = mqtt.Client()
client.username_pw_set(env.CLIENT_USERNAME, env.CLIENT_PASSWORD)
client.on_connect = mqtt_on_connect
client.on_message = mqtt_on_message
client.connect(env.MQTT_BROKER)
client.loop_forever()
