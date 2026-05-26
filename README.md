# AI Plant Disease Diagnostics System 🌿

An intelligent, computer vision-based web application designed to help farmers and agriculture enthusiasts diagnose plant diseases quickly and accurately. Built to be user-friendly, responsive, and robust without requiring any technical knowledge or user registration.

## 📌 Project Overview
This project leverages **Deep Learning** and **Computer Vision** to analyze photos of plant leaves. The system can:
- **Diagnose** the disease affecting the plant.
- **Determine Severity** (Mild, Moderate, or Severe) using advanced image segmentation.
- **Provide Recommendations** for treating the plant (pesticide/fungicide names, dosage, and prevention tips).

It is built with **Streamlit** for the frontend, ensuring accessibility on both mobile and desktop devices, and **FastAPI** coupled with **PyTorch** and **OpenCV** on the backend.

## 🚀 Key Features

### 💻 Farmer-Friendly UI (Streamlit)
- **Accessible & Responsive**: Modern interface optimized for both mobile and desktop.
- **No Registration Required**: Instantly usable without account creation.
- **Input Options**: Upload an image or capture directly via webcam.
- **Dashboard Features**:
  - Image upload & Camera capture
  - Segmentation visualization (showing diseased vs. healthy areas)
  - Severity analysis & Disease information
  - Treatment recommendations
  - Disease history tracking (current session only)

### ⚙️ Backend (FastAPI)
- **High Performance**: Fast and lightweight, capable of handling multiple requests seamlessly.
- **JSON Output**: Returns clean, formatted JSON predictions.
- **Error Handling & Logging**: Robust exception handling for invalid images and complete logging of prediction history.

### 🧠 AI & Computer Vision Pipeline
- **Disease Classification**: Uses **MobileNetV2** (fine-tuned via transfer learning on the PlantVillage dataset) for lightweight, high-accuracy inference.
- **Confidence Scoring**: Outputs the model's confidence in its diagnosis.
- **Image Segmentation (OpenCV)**: Utilizes HSV color-space segmentation to isolate healthy vs. diseased pixels, with morphological operations for noise elimination.
- **Severity Measurement**:
  - Automatically calculates severity percentage: `(Diseased Pixels / Total Leaf Pixels) × 100`
  - Classifies into: **Mild** (0–25%), **Moderate** (25–60%), **Severe** (>60%).
  - Displayed visually using progress bars and color indicators.

### 💊 Treatment Recommendation Engine
- **Rule-based Recommendations**: Maps the predicted disease and severity to actionable treatments.
- **Actionable Advice**: Provides the exact pesticide/fungicide name, dosage guidelines, application frequency, and preventive measures.

## 🛠️ Technology Stack
- **Frontend**: Streamlit
- **Backend**: Python, FastAPI
- **AI/ML**: PyTorch, Torchvision, MobileNetV2 (PlantVillage dataset)
- **Computer Vision**: OpenCV, Pillow, NumPy
- **Data Handling**: Pandas

## 📁 Project Structure
```text
leaf-disease/
│
├── backend/
│   ├── main.py                # FastAPI endpoints
│   ├── ml_model.py            # PyTorch MobileNetV2 architecture
│   ├── segmentation.py        # OpenCV HSV-based severity and masking
│   ├── recommendation.py      # Rule-based treatments engine
│   ├── utils.py               # Preprocessing pipelines
│   └── requirements.txt       
│
└── frontend/
    ├── app.py                 # Streamlit UI dashboard
    ├── utils.py               # API communication functions
    └── requirements.txt       
```

## ⚙️ Setup & Installation

### 1. Backend (FastAPI)
Open a terminal, install the required packages, and start the server:
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
*The backend API will run at `http://localhost:8000`*

### 2. Frontend (Streamlit)
Open a separate terminal, install the required packages, and run the Streamlit app:
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```
*The UI dashboard will open at `http://localhost:8501`*

## 🧠 Model Training Configuration (Overview)
- **Architecture**: Pre-trained MobileNetV2 (Transfer Learning).
- **Dataset Split**: 80% Training / 20% Validation.
- **Optimizer & Loss**: Adam optimizer, Cross-Entropy Loss.
- **Preprocessing**: RGB conversion, image resizing (224x224), and optimization for CNN inference.

> **Note:** Place your fine-tuned `.pth` weights file appropriately in the backend directory for the system to detect and load it for real-time predictions.
