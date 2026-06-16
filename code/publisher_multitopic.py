import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
client.loop_start()

try:
    while True:
        # Nilai dibuat acak di dalam loop agar terminal bergerak dinamis dan realistis
        temp = round(random.uniform(22.0, 30.0), 1)
        people = random.randint(1, 15)
        door = random.choice(["OPEN", "CLOSED"])
        
        print(f"\n[KIRIM MULTI-TOPIK] Mendistribusikan data sensor:")
        print(f" -> smartroom/room1/temperature : {temp}°C")
        client.publish("smartroom/room1/temperature", payload=f"{temp}", qos=0)
        time.sleep(1)
        
        print(f" -> smartroom/room1/people      : {people} Orang")
        client.publish("smartroom/room1/people", payload=f"{people}", qos=0)
        time.sleep(1)
        
        print(f" -> smartroom/room1/door        : {door}")
        client.publish("smartroom/room1/door", payload=door, qos=0)
        
        time.sleep(5)
except KeyboardInterrupt:
    print("\n[INFO] Menghentikan pengiriman multi-topik...")