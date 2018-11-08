import paho.mqtt.client as mqtt
import env
import car

def __str2int(val, default):
	return default if val == '' else int(val)

def mqtt_on_connect(client, userdata, flags, rc):
	client.subscribe(env.MQTT_TOPIC_RCCONTROL)
	client.subscribe(env.MQTT_TOPIC_STATUS)
	client.publish(env.MQTT_TOPIC_STATUS, env.MQTT_CONNECT_ERROR[rc])

def mqtt_on_message(client,	userdata, msg):
	if msg.topic == env.MQTT_TOPIC_RCCONTROL:
		if msg.payload[0:7] == 'forward':
			car.forward(__str2int(msg.payload[7:], env.CAR_DEFAULT_SPEED))
		elif msg.payload == 'stop':
			car.stop()
		elif msg.payload[0:8] == 'backward':
			car.backward(__str2int(msg.payload[8:], env.CAR_DEFAULT_SPEED))
		elif msg.payload[0:4] == 'left':
			car.left(__str2int(msg.payload[4:], env.CAR_DEFAULT_SPEED_DIFF))
		elif msg.payload[0:5] == 'right':
			car.right(__str2int(msg.payload[5:], env.CAR_DEFAULT_SPEED_DIFF))
		elif msg.payload == 'clockwise':
			car.clockwise()
		elif msg.payload == 'anti-clockwise':
			car.anticlockwise()
		elif msg.payload[0:5] == 'other':
			pass
			#forward()
			#forward_param(uint16_t)
			#backward()
			#backward_param(uint16_t)
			#left
			#left_param(uint16_t)
			#right
			#right_param(uint16_t)

	print("%s: %s" % (msg.topic, msg.payload))

client = mqtt.Client()
client.username_pw_set(env.CLIENT_USERNAME, env.CLIENT_PASSWORD)
client.on_connect = mqtt_on_connect
client.on_message = mqtt_on_message
client.connect(env.MQTT_BROKER)
client.loop_forever()
