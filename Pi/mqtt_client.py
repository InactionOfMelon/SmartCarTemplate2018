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
                        if msg.payload[7:] == '':
                                car.forward()
                        else:
			        car.forward_param(__str2int(msg.payload[7:], env.CAR_DEFAULT_SPEED))
		elif msg.payload == 'stop':
			car.stop()
		elif msg.payload[0:8] == 'backward':
                        if msg.payload[8:] == '':
                                car.backward()
                        else:
			        car.backward_param(__str2int(msg.payload[8:], env.CAR_DEFAULT_SPEED))
		elif msg.payload[0:4] == 'left':
                        if msg.payload[4:] == '':
                                car.left()
                        else:
                                car.left_param(__str2int(msg.payload[4:], env.CAR_DEFAULT_SPEED_DIFF))
		elif msg.payload[0:5] == 'right':
                        if msg.payload[5:] == '':
                                car.right()
                        else:
			        car.right_param(__str2int(msg.payload[5:], env.CAR_DEFAULT_SPEED_DIFF))
		elif msg.payload == 'clockwise':
			car.clockwise()
		elif msg.payload == 'anti-clockwise':
			car.anticlockwise()
		elif msg.payload[0:5] == 'other':
			pass
		
	print("%s: %s" % (msg.topic, msg.payload))

client = mqtt.Client()
client.username_pw_set(env.CLIENT_USERNAME, env.CLIENT_PASSWORD)
client.on_connect = mqtt_on_connect
client.on_message = mqtt_on_message
client.connect(env.MQTT_BROKER)
client.loop_forever()
