import paho.mqtt.client as mqtt
import env

def __str2int(val, default):
	return default if val == '' else int(val)

def mqtt_on_connect(client, userdata, flags, rc):
	print("rc %s" % (env.MQTT_CONNECT_ERROR[rc]))
	client.subscribe(env.MQTT_TOPIC_RCCONTROL)
	client.subscribe(env.MQTT_TOPIC_STATUS)
	if rc == 0:
		client.not_connected = False
	else:
		print('Reconnecting..')

def mqtt_on_message(client,	userdata, msg):
	print("%s: %s" % (msg.topic, msg.payload))
	pass

mqtt.Client.not_connected = True
client = mqtt.Client()
client.username_pw_set(env.CLIENT_USERNAME, env.CLIENT_PASSWORD)
client.on_connect = mqtt_on_connect
client.on_message = mqtt_on_message
client.connect(env.MQTT_BROKER)
client.loop_start()
