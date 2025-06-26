# 🩺 Smart Monitoring System for Neonatal Vital Signs

## 📌 Overview

This project aims to design and implement a smart real-time monitoring system for **neonatal vital signs**, using biometric sensors to measure **body temperature** and **heart rate**. The solution is focused on neonatal intensive care units (NICUs), enhancing early detection of critical conditions by continuously analyzing sensor data and generating alerts when vital signs go out of safe thresholds.

---

## 🎯 Objectives

- Collect real-time biometric data from sensors placed on newborns.
- Process and store data efficiently for real-time and historical analysis.
- Detect anomalies in temperature or heart rate using rules or ML-based logic.
- Notify healthcare staff immediately upon detecting risk conditions.

---

## ⚙️ Technical Architecture

1. **IoT Devices / Sensors**
    - Body temperature sensor (range: 34.0 – 38.5 °C)
    - Heart rate sensor (range: 100 – 160 bpm for newborns)
2. **Data Producer (Python)**
    - Simulates sensor signals (for demo) or consumes from real devices.
    - Sends data to a **Kafka** topic or **MQTT** broker.
3. **Data Ingestion Layer**
    - Apache Kafka or MQTT as the messaging queue.
    - Optional REST API for HTTP-based ingestion.
4. **Stream Processing**
    - Real-time processing using Apache **Spark Streaming** or **Flink**.
    - Applies threshold checks and anomaly detection.
5. **Storage**
    - **Short-term**: NoSQL database (e.g., InfluxDB or MongoDB) for real-time dashboards.
    - **Long-term**: S3, HDFS, or PostgreSQL for historical data analytics.
6. **Visualization**
    - Live dashboards using **Grafana** or **Streamlit**.
    - Displays real-time charts, alerts, and historical trends.
7. **Alert System**
    - Alerts via email, SMS, or push notifications when values exceed safe limits.

---

## 📊 Sample Sensor Data (JSON)

```json
{
  "sensor_id": "neonate_001",
  "timestamp": "2025-06-26T15:21:00Z",
  "temperature": 37.1,
  "heart_rate": 142,
  "status": "normal"
}

```

## 🚨 Alert Thresholds

| Parameter | Normal Range | Alert Thresholds |
| --- | --- | --- |
| Temperature (°C) | 36.5 – 37.5 | <36.0 or >38.0 |
| Heart Rate (bpm) | 110 – 160 | <100 or >180 |

---

## 🌐 Use Cases

- Neonatal Intensive Care Units (NICU)
- Remote monitoring in rural hospitals
- Home monitoring for early-discharged infants

---

## 🚀 Future Extensions

- Predictive models for sepsis or apnea detection
- Integration with oxygen saturation or respiratory rate sensors
- Mobile app for caregivers and medical personnel
