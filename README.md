# 🪴 Plant Disease Detection API (YOLOv8 & FastAPI)

This project is a production-ready **Artificial Intelligence Microservice (Backend)** architecture designed to classify plant leaf diseases. It leverages an optimized **YOLOv8 (YOLOv8n-cls)** image classification model trained on a custom dataset and exposes it via a high-performance REST API.

To eliminate environment mismatch issues ("it works on my machine") and ensure platform-independent scalability, the entire application is fully **Dockerized** and continuously deployed on **Hugging Face Spaces** (Docker SDK).

---

## 🚀 Live API & Documentation
* **Interactive API Documentation :** `https://musashivulpix-plant-disease-cv-system.hf.space/docs`

---

## 🛠️ Architecture & Tech Stack

The system is engineered following modern MLOps (Machine Learning Operations) best practices, featuring a layered and decoupled architecture:

* **AI & Computer Vision Core:** Ultralytics YOLOv8n-cls (utilizing a custom-trained `best.pt` weights file).
* **Web Framework:** FastAPI (chosen for its asynchronous capabilities, high concurrency performance, and native OpenAPI/Swagger integration).
* **ASGI Server:** Uvicorn (lightning-fast production web server).
* **Containerization:** Docker (utilizing a highly optimized Debian Slim base image).
* **Image Processing:** OpenCV (OpenCV-Python) & Pillow.
* **Cloud Deployment:** Hugging Face Spaces Cloud Infrastructure.

---

## 📦 Project Structure

```text
.
├── weights/
│   └── best.pt          # Custom-trained YOLOv8 classification weights
├── main.py              # FastAPI application core & inference logic
├── Dockerfile           # Layered Docker image configuration
├── requirements.txt     # Python dependency manifest
└── README.md            # Project documentation
