import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("[INFO] Mendaftarkan multi-topik paralel secara terpisah...\n" + "-"*60)
    client.subscribe("smartroom/room1/temperature")
    client.subscribe("smartroom/room1/people")
    client.subscribe("smartroom/room1/door")

def on_message(client, userdata, msg):
    payload_data = msg.payload.decode()
    print(f"[DATA MASUK] Alamat Topik: {msg.topic} -> Nilai: {payload_data}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_forever()