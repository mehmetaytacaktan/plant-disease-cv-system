# Plant Disease Computer Vision System 🍃

An end-to-end Computer Vision pipeline designed for precision agriculture to detect plant leaf diseases and nutrient deficiencies. Built with **YOLOv8**, served via **FastAPI**, and production-ready with **Docker**.

## 🛠️ Tech Stack & Architecture
* **Model:** YOLOv8 (Fine-tuned via Transfer Learning on the PlantVillage dataset)
* **Backend:** FastAPI (Asynchronous REST API)
* **DevOps:** Docker, VPS Deployment, Nginx

---

## 🚀 System Architecture
1. **Data Pipeline:** Preprocessing plant leaf images and training a custom YOLOv8 classification model using Google Colab (T4 GPU).
2. **API Layer:** Serving the model weights (`.pt`) via a high-performance, asynchronous FastAPI backend.
3. **Containerization:** Packaging the runtime environment into a lightweight Docker container for seamless deployment.

---

## 📌 Roadmap & Current Status
- [x] GitHub Repository Setup & Profile Alignment
- [x] Model Training & Hyperparameter Tuning (YOLOv8)
- [x] FastAPI Backend Development & Local Testing 
- [ ] Dockerization & Local Container Tests <!-- Current Stage -->
- [ ] Remote VPS Deployment & Nginx Reverse Proxy Configuration
