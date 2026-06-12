# 🏡 Smart Room Monitoring with MQTT Protocol

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![MQTT](https://img.shields.io/badge/Protocol-MQTT-green)
![Mosquitto](https://img.shields.io/badge/Broker-Mosquitto-orange)
![paho-mqtt](https://img.shields.io/badge/Library-paho--mqtt-red)

Implementasi komunikasi MQTT menggunakan Python dan Mosquitto Broker untuk mensimulasikan sistem pemantauan kondisi ruangan secara real-time pada lingkungan Cyber Physical System (CPS).

---

# 📖 Project Overview

Proyek ini bertujuan untuk mempelajari mekanisme komunikasi berbasis MQTT dengan menerapkan pola publish-subscribe pada studi kasus Smart Room Monitoring.

Pada sistem ini, publisher berperan sebagai sensor virtual yang menghasilkan data:

* 🌡️ Temperature
* 💧 Humidity
* 💡 Light Intensity

Data dikirim ke Mosquitto Broker menggunakan beberapa topic MQTT, kemudian diterima oleh subscriber sebagai aplikasi monitoring.

Selain komunikasi dasar, sistem juga mengimplementasikan:

* QoS Level 0
* QoS Level 1
* QoS Level 2
* Multiple Topic Communication
* Wildcard Topic (+)
* Wildcard Topic (#)

---

# 🎯 Learning Objectives

* Memahami konsep MQTT pada Cyber Physical System
* Mengimplementasikan Publisher dan Subscriber menggunakan Python
* Menggunakan Mosquitto sebagai MQTT Broker
* Menguji pengaruh QoS terhadap pengiriman pesan
* Menggunakan struktur topic bertingkat
* Menerapkan wildcard MQTT (+ dan #)
* Menganalisis distribusi pesan pada berbagai skenario komunikasi

---

# 🏗️ System Architecture

Tambahkan gambar:

```text
docs/system_architecture.png
```

## Communication Flow

1. Virtual Sensor menghasilkan data monitoring ruangan
2. Publisher mengirimkan data ke Mosquitto Broker
3. Broker menerima dan mengelola pesan berdasarkan topic
4. Subscriber melakukan subscribe pada topic tertentu
5. Broker mendistribusikan pesan yang sesuai
6. Monitoring Application menampilkan data secara real-time

---

# 📡 MQTT Topic Structure

smartroom/room1/temperature

smartroom/room1/humidity

smartroom/room1/light

smartroom/room1/qos

## Wildcard Topics

smartroom/+/temperature

smartroom/#

---

# ⚙️ Technologies Used

| Component              | Technology        |
| ---------------------- | ----------------- |
| Programming Language   | Python 3          |
| MQTT Library           | paho-mqtt         |
| Message Broker         | Mosquitto         |
| Communication Protocol | MQTT              |
| Architecture           | Publish-Subscribe |

---

# 📂 Project Structure

mqtt-smartroom-aqilah/

├── src/

│ ├── scenario1_basic/

│ ├── scenario2_qos/

│ ├── scenario3_multitopic/

│ ├── scenario4_wildcard_plus/

│ └── scenario5_wildcard_hash/

│

├── docs/

│ ├── system_architecture.png

│ └── laporan.pdf

│

├── screenshots/

│ ├── scenario1/

│ ├── scenario2/

│ ├── scenario3/

│ ├── scenario4/

│ └── scenario5/

│

├── requirements.txt

└── README.md

---

# 🚀 Installation

## 1. Install Mosquitto Broker

### Windows

Download dan install Mosquitto Broker.

### Ubuntu / Debian

```bash
sudo apt install mosquitto
sudo systemctl start mosquitto
```

---

## 2. Install Dependencies

```bash
pip install paho-mqtt
```

atau

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Mosquitto Broker

```bash
mosquitto -v
```

Jika berhasil:

```text
Opening ipv4 listen socket on port 1883
Opening ipv6 listen socket on port 1883
```

---

# 🧪 Test Scenarios

## Scenario 1 — Basic Publisher & Subscriber

Subscriber:

```bash
python src/scenario1_basic/subscriber_basic.py
```

Publisher:

```bash
python src/scenario1_basic/publisher_basic.py
```

---

## Scenario 2 — Quality of Service (QoS)

```bash
python src/scenario2_qos/subscriber_qos.py
```

```bash
python src/scenario2_qos/publisher_qos.py
```

---

## Scenario 3 — Multiple Topics

```bash
python src/scenario3_multitopic/subscriber_multitopic.py
```

```bash
python src/scenario3_multitopic/publisher_multitopic.py
```

---

## Scenario 4 — Wildcard (+)

```bash
python src/scenario4_wildcard_plus/subscriber_plus.py
```

```bash
python src/scenario4_wildcard_plus/publisher_plus.py
```

---

## Scenario 5 — Wildcard (#)

```bash
python src/scenario5_wildcard_hash/subscriber_hash.py
```

```bash
python src/scenario5_wildcard_hash/publisher_hash.py
```

# 💡 Notes

* Jalankan Mosquitto Broker terlebih dahulu
* Jalankan Subscriber sebelum Publisher
* Gunakan terminal terpisah untuk setiap proses
* Tekan Ctrl+C untuk menghentikan program

---

# 🚨 Troubleshooting

| Error               | Solution                       |
| ------------------- | ------------------------------ |
| mosquitto not found | Tambahkan Mosquitto ke PATH    |
| Connection Refused  | Pastikan Broker berjalan       |
| ModuleNotFoundError | Install paho-mqtt              |
| No message received | Jalankan subscriber lebih dulu |

---

# 📊 MQTT Features Implemented

✅ Publish-Subscribe Pattern

✅ QoS Level 0, 1, 2

✅ Multiple Topic Communication

✅ Wildcard Topic (+)

✅ Wildcard Topic (#)

✅ Real-Time Monitoring

---

# 👩‍💻 Author

Aqilah Akma

NIM: 235150301111017

Teknik Komputer

Universitas Brawijaya

---

# 📜 License

Project ini dibuat untuk keperluan akademik pada mata kuliah Cyber Physical System (CPS).

2026
