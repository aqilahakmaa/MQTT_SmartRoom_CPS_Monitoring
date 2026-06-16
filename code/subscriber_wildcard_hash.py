import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("[INFO] Mengaktifkan pusat pemantauan/Logger Global: smartroom/#\n" + "-"*60)
    client.subscribe("smartroom/#")

def on_message(client, userdata, msg):
    payload_data = msg.payload.decode()
    print(f"[LOG GLOBAL] Topik Asal: {msg.topic} | Payload Data: {payload_data}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_forever()