import paho.mqtt.client as mqtt
import time

def __str2int(val, default):
	return default if val == '' else int(val)
MQTT_CONNECT_ERROR = ("0: Connection successful", "1: Connection refused - incorrect protocol version", "2: Connection refused - invalid client identifier", "3: Connection refused - server unavailable", "4: Connection refused - bad username or password", "5: Connection refused - not authorised")
def mqtt_on_connect(client, userdata, flags, rc):
	print("rc %s" % (MQTT_CONNECT_ERROR[rc]))
	if rc == 0:
		client.not_connected = False
	else:
		print('Reconnecting...')

def mqtt_on_message(client,	userdata, msg):
#	print("%s (%d): %s" % (msg.topic, msg.qos, msg.payload))
	pass

mqtt.Client.not_connected = True
client = mqtt.Client()
client.username_pw_set('smartcar', 'smartcar')
client.on_connect = mqtt_on_connect
# client.on_message = mqtt_on_message
client.connect('mqtt.gycis.me', port = 1883)
client.loop_start()
while client.not_connected:
	pass

title = '/smartcar/dd0686/'
topics = {
	't': title + 'task'
,	'c': title + 'command'
#,	'p': title + 'position' 
}
while True:
	print('Available topics:')
	print('  t: task')
	print('  c: command')
	#print('  p: position')
	topic = input("topic: ")
	if topic in topics:
		if topic == 't':
			s = int(input('start: '))
			t = int(input('end: '))
			data = bytes([s, t])
		elif topic == 'c':
			print('0: start; 1: end; 2: error')
			c = int(input('command: '))
			data = bytes([c])
		client.publish(topics[topic], data, 1)
	else:
		print('Invalid topic:', topic)
