import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("[INFO] Mengaktifkan filter jaminan paket data ruangan (QoS 0, 1, 2).\n" + "-"*60)
    client.subscribe("smartroom/room1/qos_test", qos=2)

def on_message(client, userdata, msg):
    payload_data = msg.payload.decode()
    print(f"[TERIMA - QoS {msg.qos}] Data: {payload_data}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_forever()