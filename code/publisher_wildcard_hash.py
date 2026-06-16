import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
client.loop_start()

try:
    while True:
        temp = round(random.uniform(21.0, 25.0), 1)
        people = random.randint(1, 10)
        door = random.choice(["OPEN", "CLOSED"])
        
        print(f"\n[PUBLISH GLOBAL] Menyiarkan seluruh aktivitas sensor ruangan:")
        print(f" -> smartroom/room1/temperature : {temp}")
        client.publish("smartroom/room1/temperature", payload=f"{temp}°C", qos=0)
        time.sleep(1)
        
        print(f" -> smartroom/room1/people      : {people}")
        client.publish("smartroom/room1/people", payload=f"{people} Orang", qos=0)
        time.sleep(1)
        
        print(f" -> smartroom/room1/door        : {door}")
        client.publish("smartroom/room1/door", payload=door, qos=0)
        
        time.sleep(5)
except KeyboardInterrupt:
    print("\n[INFO] Menutup sistem sebaran data global...")