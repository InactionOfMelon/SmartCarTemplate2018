MQTT_BROKER = "mqtt.gycis.me"
MQTT_TOPIC_ID = "inactionofmelon"
MQTT_TOPIC_RCCONTROL = "/smartcar/" + MQTT_TOPIC_ID + "/rccontrol"
MQTT_TOPIC_STATUS = "/smartcar/" + MQTT_TOPIC_ID + "/status"
MQTT_QOS = 1

CLIENT_USERNAME = "smartcar"
CLIENT_PASSWORD = "smartcar"

CAR_DEFAULT_SPEED = -1
CAR_DEFAULT_SPEED_DIFF = -1

MQTT_CONNECT_ERROR = ("0: Connection successful", "1: Connection refused - incorrect protocol version", "2: Connection refused - invalid client identifier", "3: Connection refused - server unavailable", "4: Connection refused - bad username or password", "5: Connection refused - not authorised")

