import paho.mqtt.client as mqtt
import time
import env

is_connected = False

def __str2int(val, default):
	return default if val == '' else int(val)

def mqtt_on_connect(client, userdata, flags, rc):
#	client.subscribe(env.MQTT_TOPIC_RCCONTROL)
	client.subscribe(env.MQTT_TOPIC_STATUS)
	print("rc %s" % (env.MQTT_CONNECT_ERROR[rc]))
	if rc == 0:
		global is_connected
		is_connected = True
	else:
		exit(rc)

def mqtt_on_message(client,	userdata, msg):
#	print("%s (%d): %s" % (msg.topic, msg.qos, msg.payload))
	pass

client = mqtt.Client()
client.username_pw_set(env.CLIENT_USERNAME, env.CLIENT_PASSWORD)
client.on_connect = mqtt_on_connect
# client.on_message = mqtt_on_message
client.connect(env.MQTT_BROKER)
client.loop_start()

while True:
	if is_connected:
		text = raw_input("publish: ")
		client.publish(env.MQTT_TOPIC_RCCONTROL, text, 1)
