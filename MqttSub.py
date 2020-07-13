import paho.mqtt.client as mqtt

# MQTT_SERVER is the IP address
MQTT_SERVER = 'localhost'

# MQTT_PATH is the channel's name
MQTT_PATH = 'test'


def onConnect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_PATH)


def onMessage(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = onConnect
client.on_message = onMessage

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()
