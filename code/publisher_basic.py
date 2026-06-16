import paho.mqtt.client as mqtt
import time

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
print("[INFO] Menghubungkan ke Mosquitto Broker lokal...")
client.connect("localhost", 1883)
client.loop_start()

try:
    while True:
        val_temp = "26.5"
        topic = "smartroom/room1/temperature"
        print(f"[PUBLISH] Mengirim data suhu ke {topic} -> {val_temp}°C")
        client.publish(topic, payload=val_temp, qos=0)
        time.sleep(5)
except KeyboardInterrupt:
    print("\n[INFO] Memutus koneksi publisher...")