import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
client.loop_start()

try:
    while True:
        print("\n=== MEMULAI SIKLUS PENGUJIAN AKURASI DATA (QoS) ===")
        # Nilai diacak di dalam loop agar berubah di setiap baris cetakan
        temp = round(random.uniform(24.0, 29.0), 1)
        
        # Masing-masing data dikirim ke topik 'smartroom/room1/qos_test'
        print(f"[QoS 0 Sent] Mengirim telemetri suhu -> {temp}°C")
        client.publish("smartroom/room1/qos_test", payload=f"Suhu: {temp}°C", qos=0)
        time.sleep(2)
        
        print(f"[QoS 1 Sent] Mengirim data jumlah orang -> 5 orang")
        client.publish("smartroom/room1/qos_test", payload="Orang: 5", qos=1)
        time.sleep(2)
        
        print(f"[QoS 2 Sent] Mengirim status akses pintu -> CLOSED")
        client.publish("smartroom/room1/qos_test", payload="Pintu: CLOSED", qos=2)
        
        time.sleep(5)
except KeyboardInterrupt:
    print("\n[INFO] Menghentikan simulasi pengujian QoS...")