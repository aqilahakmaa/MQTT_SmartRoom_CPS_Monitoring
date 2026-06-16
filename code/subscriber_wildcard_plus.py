import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("[INFO] Menghubungkan ke broker Mosquitto.")
    print("[INFO] Menunggu data dengan filter satu tingkat: smartroom/+/temperature\n" + "-"*60)
    client.subscribe("smartroom/+/temperature")

def on_message(client, userdata, msg):
    payload_data = msg.payload.decode()
    print(f"[FILTER + MATCH] Jalur: {msg.topic} -> Nilai Terbaca: {payload_data}°C")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_forever()