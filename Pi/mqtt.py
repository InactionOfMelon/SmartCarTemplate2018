import time
import re
import paho.mqtt.client as mqtt

MQTT_CONNECT_ERROR = ("0: Connection successful", "1: Connection refused - incorrect protocol version", "2: Connection refused - invalid client identifier", "3: Connection refused - server unavailable", "4: Connection refused - bad username or password", "5: Connection refused - not authorised")
with open('/sys/class/net/wlan0/address') as f:
	title = '/smartcar/' + re.sub(r'.+((:\w\w){3})\n',r'\1', f.read()).replace(':', '') + '/'
print('mqtt: title:', title)

topics = {
	'task': title + 'task'
,	'command': title + 'command'
#,	'position': title + 'position'
}

mqtt.Client.not_connected = True
class MQTT:
	def task_dealer(self, msg):
		self.data.vertices.update({'s': msg.payload[0], 't': msg.payload[1]})#, 'u': msg.payload[0]})
	def command_dealer(self, msg):
		if msg.payload[0] == 0x00:
			self.data.status = 1
			print('mqtt:', 'car started')
		elif msg.payload[0] == 0x01:
			self.data.status = 2
			print('mqtt:', 'car ended')
		elif msg.payload[0] == 0x02:
			self.data.status = -1
			print('mqtt:', 'car error')
	def position_dealer(self, msg):
		u, v, d = msg.payload[0], msg.payload[1], msg.payload[3] * 0xFF + msg.payload[2]
		w = self.data.weight[u][v]
		self.data.vertices['u'] = u if d * 2 < w else v
	def on_message(self, client, userdata, msg):
		if msg.topic == topics['task']:
			self.task_dealer(msg)
		elif msg.topic == topics['command']:
			self.command_dealer(msg)
		#elif msg.topic == topics['position']:
		#	self.position_dealer(msg)
		#print("%s: %s" % (msg.topic, msg.payload))
	def on_connect(self, client, userdata, flags, rc):
		for key in topics:
			self.client.subscribe(topics[key])
		print('mqtt:', MQTT_CONNECT_ERROR[rc])
		if rc == 0:
			self.client.not_connected = False
		else:
			print('mqtt:', 'reconnecting...')
	def __init__(self, data):
		self.data = data
		self.client = mqtt.Client()
		self.client.not_connected = True
		self.client.username_pw_set('smartcar', 'smartcar')
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message
		self.client.connect('mqtt.gycis.me', port = 1883)
		self.client.loop_start()

def __str2int(val, default):
	return default if val == '' else int(val)

