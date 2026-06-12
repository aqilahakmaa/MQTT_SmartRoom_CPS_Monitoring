# 🏠 MQTT Smart Room Monitoring

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Mosquitto](https://img.shields.io/badge/Mosquitto-Latest-green)
![Protocol](https://img.shields.io/badge/Protocol-MQTT-orange)
![Library](https://img.shields.io/badge/Library-paho--mqtt-yellow)
![Course](https://img.shields.io/badge/Course-Cyber%20Physical%20System-red)

# 🏠 MQTT Smart Room Monitoring

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Mosquitto](https://img.shields.io/badge/Mosquitto-Latest-green)
![Protocol](https://img.shields.io/badge/Protocol-MQTT-orange)
![Library](https://img.shields.io/badge/Library-paho--mqtt-yellow)
![Course](https://img.shields.io/badge/Course-Cyber%20Physical%20System-red)

Implementasi sistem komunikasi MQTT untuk Smart Room Monitoring menggunakan Python dan Mosquitto Broker.

---

# 📋 Deskripsi Singkat

Project ini merupakan implementasi komunikasi MQTT menggunakan Python dan Mosquitto Broker pada studi kasus Smart Room Monitoring. Sistem menggunakan pola komunikasi publish-subscribe, dimana publisher berperan sebagai sensor virtual yang mengirimkan data temperature, humidity, dan light ke broker MQTT. Selanjutnya subscriber menerima data tersebut untuk keperluan monitoring secara real-time.

---

# 🏗️ Arsitektur Sistem

```text
Temperature Sensor
Humidity Sensor
Light Sensor

        |
        |
        v

+------------------+
| Publisher Python |
+------------------+

        |
        |
        v

+------------------+
| Mosquitto Broker |
+------------------+

        |
        |
        v

+------------------+
| Subscriber       |
| Monitoring App   |
+------------------+
```

## Alur Komunikasi

1. Publisher mengumpulkan data sensor virtual (temperature, humidity, light).
2. Publisher mengirimkan data ke Mosquitto Broker melalui topic MQTT.
3. Mosquitto Broker menerima dan mendistribusikan pesan.
4. Subscriber melakukan subscribe pada topic tertentu.
5. Broker meneruskan pesan kepada subscriber yang sesuai.
6. Subscriber menerima data monitoring secara real-time.

---

# 🛠️ Tech Stack

| Komponen           | Teknologi                                  |
| ------------------ | ------------------------------------------ |
| Bahasa Pemrograman | Python 3.10+                               |
| Message Broker     | Mosquitto Broker                           |
| MQTT Library       | paho-mqtt                                  |
| Protocol           | MQTT (Message Queuing Telemetry Transport) |

---

# 📂 Struktur Topic MQTT

```text
smartroom/room1/temperature
smartroom/room1/humidity
smartroom/room1/light
```

Wildcard yang digunakan:

```text
smartroom/+/temperature
smartroom/#
```

---

# 📁 Struktur Proyek

```text
MQTT_SmartRoom_CPS_Monitoring/
├── source_code/
│   ├── subscriber_basic.py
│   ├── publisher_basic.py
│   ├── subscriber_qos.py
│   ├── publisher_qos.py
│   ├── subscriber_multitopic.py
│   ├── publisher_multitopic.py
│   ├── subscriber_wildcard_plus.py
│   ├── publisher_wildcard_plus.py
│   ├── subscriber_wildcard_hash.py
│   └── publisher_wildcard_hash.py
├── screenshots/
├── diagrams/
├── laporan/
├── README.md
└── requirements.txt
```

---

# 🚀 Quick Start

## 0️⃣ Install Mosquitto Broker

### Windows

Download dari:

https://mosquitto.org/download/

Install menggunakan konfigurasi default.

### Linux (Ubuntu/Debian)

```bash
sudo apt-get install mosquitto
sudo systemctl start mosquitto
```

---

## 1️⃣ Instalasi Dependencies

```bash
pip install paho-mqtt
```

atau

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Jalankan Mosquitto Broker

```bash
mosquitto -v
```

Broker akan berjalan pada:

```text
localhost:1883
```

---

# 📚 Skenario dan Cara Menjalankan

## Skenario 1 - Basic Publisher Subscriber

```bash
# Terminal 1
mosquitto -v

# Terminal 2
python source_code/subscriber_basic.py

# Terminal 3
python source_code/publisher_basic.py
```

---

## Skenario 2 - Quality of Service (QoS)

```bash
# Terminal 1
mosquitto -v

# Terminal 2
python source_code/subscriber_qos.py

# Terminal 3
python source_code/publisher_qos.py
```

---

## Skenario 3 - Multiple Topic

```bash
# Terminal 1
mosquitto -v

# Terminal 2
python source_code/subscriber_multitopic.py

# Terminal 3
python source_code/publisher_multitopic.py
```

---

## Skenario 4 - Wildcard (+)

```bash
# Terminal 1
mosquitto -v

# Terminal 2
python source_code/subscriber_wildcard_plus.py

# Terminal 3
python source_code/publisher_wildcard_plus.py
```

---

## Skenario 5 - Wildcard (#)

```bash
# Terminal 1
mosquitto -v

# Terminal 2
python source_code/subscriber_wildcard_hash.py

# Terminal 3
python source_code/publisher_wildcard_hash.py
```

---

# 💡 Tips Menjalankan

* Jalankan Mosquitto Broker terlebih dahulu.
* Jalankan Subscriber sebelum Publisher.
* Gunakan minimal tiga terminal.
* Gunakan Ctrl + C untuk menghentikan program.

---

# ⚠️ Troubleshooting

| Error                           | Penyebab                        | Solusi                                  |
| ------------------------------- | ------------------------------- | --------------------------------------- |
| Command 'mosquitto' not found   | Mosquitto belum terinstall      | Install Mosquitto dan tambahkan ke PATH |
| Connection Refused              | Broker belum berjalan           | Jalankan mosquitto -v                   |
| ModuleNotFoundError: paho       | Library belum terinstall        | pip install paho-mqtt                   |
| Subscriber tidak menerima pesan | Subscriber dijalankan terlambat | Jalankan subscriber terlebih dahulu     |

---

# 📊 Konsep MQTT yang Diimplementasikan

✅ Publish-Subscribe Pattern

✅ Quality of Service (QoS 0, 1, 2)

✅ Multiple Topics

✅ Wildcard Subscription (+)

✅ Wildcard Subscription (#)

✅ Real-Time Communication

✅ Cyber Physical System Communication

---

# 👤 Author

Aqilah Akma

NIM: 235150301111017

Teknik Komputer

Fakultas Ilmu Komputer

Universitas Brawijaya

---

# 📝 License

Project ini dibuat untuk keperluan akademis pada mata kuliah Cyber Physical System (CPS).

Last Updated: 2026

Smart Room Monitoring System via MQTT

