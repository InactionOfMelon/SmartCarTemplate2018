import paho.mqtt.client as mqtt
import time
import env

def __str2int(val, default):
	return default if val == '' else int(val)

def mqtt_on_connect(client, userdata, flags, rc):
#	client.subscribe(env.MQTT_TOPIC_RCCONTROL)
	client.subscribe(env.MQTT_TOPIC_STATUS)
	print("rc %s" % (env.MQTT_CONNECT_ERROR[rc]))
	if rc == 0:
		client.not_connected = False
	else:
		print('Reconnecting...')

def mqtt_on_message(client,	userdata, msg):
#	print("%s (%d): %s" % (msg.topic, msg.qos, msg.payload))
	pass

mqtt.Client.not_connected = True
client = mqtt.Client()
client.username_pw_set(env.CLIENT_USERNAME, env.CLIENT_PASSWORD)
client.on_connect = mqtt_on_connect
# client.on_message = mqtt_on_message
client.connect(env.MQTT_BROKER)
client.loop_start()
while client.not_connected:
	pass

while True:
	text = input("publish: ")
	client.publish(env.MQTT_TOPIC_RCCONTROL, text, 1)
