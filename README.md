# 🏡 Smart Room Monitoring System

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![MQTT](https://img.shields.io/badge/Protocol-MQTT-green)
![Mosquitto](https://img.shields.io/badge/Broker-Mosquitto-orange)
![paho-mqtt](https://img.shields.io/badge/Library-paho--mqtt-red)
![CPS](https://img.shields.io/badge/Course-Cyber%20Physical%20System-purple)

Implementasi komunikasi MQTT menggunakan Python dan Mosquitto Broker untuk sistem Smart Room Monitoring berbasis Cyber Physical System (CPS).

---

# 📖 Deskripsi Singkat

Project ini merupakan implementasi protokol MQTT menggunakan Python dan Mosquitto Broker pada studi kasus Smart Room Monitoring.

Sistem mensimulasikan sebuah ruangan pintar menggunakan beberapa sensor virtual yang menghasilkan data secara real-time. Data dikirim melalui MQTT Broker menggunakan pola komunikasi publish-subscribe dan diterima oleh aplikasi monitoring.

Parameter yang dimonitor meliputi:

- 🌡️ Temperature Sensor
- 👥 People Count Sensor
- 🚪 Door Status Sensor

Selain komunikasi dasar publisher dan subscriber, sistem juga mengimplementasikan berbagai fitur MQTT seperti Quality of Service (QoS), Multiple Topic, Wildcard (+), dan Wildcard (#).

---

# 🎯 Tujuan Proyek

- Memahami konsep MQTT pada Cyber Physical System.
- Mengimplementasikan Publisher dan Subscriber menggunakan Python.
- Menggunakan Mosquitto sebagai MQTT Broker.
- Menguji QoS Level 0, QoS Level 1, dan QoS Level 2.
- Menggunakan struktur topic MQTT bertingkat.
- Mengimplementasikan wildcard topic (+) dan (#).
- Menganalisis proses distribusi pesan MQTT.

---

# 🏗️ Arsitektur Sistem

<p align="center">
  <img src="Arsitektur%20SmartDoor.jpg" width="1000">
</p>

## Alur Komunikasi

1. Temperature Sensor, People Count Sensor, dan Door Status Sensor menghasilkan data virtual.
2. Publisher Python mengumpulkan data dari sensor virtual.
3. Data dipublikasikan ke Mosquitto MQTT Broker menggunakan topic tertentu.
4. Broker menerima dan mendistribusikan pesan kepada subscriber yang sesuai.
5. Subscriber menerima data dari broker.
6. Monitoring Dashboard menampilkan informasi ruangan secara real-time.

---

# 📡 Struktur Topic MQTT

Topic yang digunakan:

```text
smartroom/room1/temperature
smartroom/room1/people
smartroom/room1/door
```

Wildcard Topic:

```text
smartroom/+/temperature
smartroom/#
```

---

# ⚙️ Tech Stack

| Komponen | Teknologi |
|-----------|-----------|
| Programming Language | Python 3 |
| Protocol | MQTT |
| Message Broker | Mosquitto Broker |
| MQTT Library | paho-mqtt |
| Communication Model | Publish-Subscribe |

---

# 📁 Struktur Proyek

```text
MQTT_SmartRoom_CPS_Monitoring/
│
├── code/
│   ├── publisher_basic.py
│   ├── subscriber_basic.py
│   ├── publisher_qos.py
│   ├── subscriber_qos.py
│   ├── publisher_multitopic.py
│   ├── subscriber_multitopic.py
│   ├── publisher_wildcard_plus.py
│   ├── subscriber_wildcard_plus.py
│   ├── publisher_wildcard_hash.py
│   └── subscriber_wildcard_hash.py
│
├── screenshots/
│
├── docs/
│   └── system_architecture.png
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Quick Start

## 1️⃣ Install Mosquitto Broker

### Windows

Download:

https://mosquitto.org/download/

Install menggunakan konfigurasi default.

### Ubuntu / Debian

```bash
sudo apt install mosquitto
sudo systemctl start mosquitto
```

---

## 2️⃣ Install Dependency

```bash
pip install paho-mqtt
```

atau

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Jalankan Mosquitto Broker

```bash
mosquitto -v
```

Jika berhasil akan muncul:

```text
Opening ipv4 listen socket on port 1883
Opening ipv6 listen socket on port 1883
```

---

# 🧪 Skenario Pengujian

## Skenario 1 — Komunikasi Dasar Publisher-Subscriber

```bash
python code/subscriber_basic.py
```

```bash
python code/publisher_basic.py
```

---

## Skenario 2 — Quality of Service (QoS)

```bash
python code/subscriber_qos.py
```

```bash
python code/publisher_qos.py
```

---

## Skenario 3 — Multiple Topic

```bash
python code/subscriber_multitopic.py
```

```bash
python code/publisher_multitopic.py
```

---

## Skenario 4 — Wildcard (+)

```bash
python code/subscriber_wildcard_plus.py
```

```bash
python code/publisher_wildcard_plus.py
```

---

## Skenario 5 — Wildcard (#)

```bash
python code/subscriber_wildcard_hash.py
```

```bash
python code/publisher_wildcard_hash.py
```

---

# 📸 Dokumentasi Pengujian

Folder `screenshots/` berisi hasil pengujian untuk setiap skenario implementasi MQTT.

- Basic Publisher-Subscriber
- QoS 0, 1, dan 2
- Multiple Topic
- Wildcard (+)
- Wildcard (#)

---

# 💡 Tips Menjalankan

- Jalankan Mosquitto Broker terlebih dahulu.
- Jalankan Subscriber sebelum Publisher.
- Gunakan terminal yang berbeda untuk Broker, Subscriber, dan Publisher.
- Tekan Ctrl + C untuk menghentikan program.

---

# 🚨 Troubleshooting

| Error | Solusi |
|---------|---------|
| mosquitto not found | Tambahkan Mosquitto ke PATH |
| Connection Refused | Pastikan Broker berjalan |
| ModuleNotFoundError | Install paho-mqtt |
| Subscriber tidak menerima pesan | Jalankan subscriber terlebih dahulu |

---

# 📊 Konsep MQTT yang Diimplementasikan

✅ Publish-Subscribe Pattern

✅ QoS Level 0, 1, dan 2

✅ Multiple Topic Communication

✅ Wildcard Topic (+)

✅ Wildcard Topic (#)

✅ Real-Time Monitoring

---

# 👩‍💻 Author

Nama : **Aqilah Akma**  
NIM  : **235150301111017**

Teknik Komputer  
Fakultas Ilmu Komputer  
Universitas Brawijaya

---

# 📜 License

Project ini dibuat untuk keperluan akademik pada mata kuliah Cyber Physical System (CPS).

2026
