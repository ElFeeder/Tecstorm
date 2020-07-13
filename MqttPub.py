import paho.mqtt.publish as publish


MQTT_SERVER = 'localhost'
MQTT_PATH = 'test'

publish.single(MQTT_PATH, "Drena", hostname = MQTT_SERVER)
