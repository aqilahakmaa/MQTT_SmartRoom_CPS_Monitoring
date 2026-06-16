import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
client.loop_start()

try:
    while True:
        temp_r1 = round(random.uniform(23.0, 26.0), 1)
        temp_r2 = round(random.uniform(24.0, 27.0), 1)
        
        print(f"\n[PUBLISH SKENARIO 4] Menyebarkan data ke broker:")
        print(f" -> Kirim ke smartroom/room1/temperature : {temp_r1}")
        client.publish("smartroom/room1/temperature", payload=str(temp_r1), qos=0)
        time.sleep(1)
        
        print(" -> Kirim ke smartroom/room1/door        : OPEN (Harusnya terblokir di Subscriber)")
        client.publish("smartroom/room1/door", payload="OPEN", qos=0)
        time.sleep(1)
        
        print(f" -> Kirim ke smartroom/room2/temperature : {temp_r2}")
        client.publish("smartroom/room2/temperature", payload=str(temp_r2), qos=0)
        
        time.sleep(5)
except KeyboardInterrupt:
    print("\n[INFO] Menghentikan pengisian data wildcard plus...")