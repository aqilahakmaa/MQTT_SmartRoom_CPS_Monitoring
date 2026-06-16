import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("[INFO] Berhasil terhubung ke broker Mosquitto.")
    print("[SUBSCRIBE] Menunggu kiriman data dari topik suhu...\n" + "-"*60)
    client.subscribe("smartroom/room1/temperature")

def on_message(client, userdata, msg):
    payload_data = msg.payload.decode()
    print(f"[SUBSCRIBE] Data diterima dari {msg.topic} -> Suhu: {payload_data}°C")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_forever()