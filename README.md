# AI Plant Disease Diagnostics System 🌿

This project is an end-to-end AI plant disease diagnostics system. It uses **Streamlit** for a modern frontend and **FastAPI** coupled with **PyTorch (MobileNetV2)** and **OpenCV** for backend processing. 

## Features
- **Dashboard & UI**: Built with Streamlit for a responsive, modern user experience.
- **Image Input**: Upload images or capture directly via webcam.
- **Disease Classification**: PyTorch-based inference pipeline using a MobileNetV2 architecture (pre-configured for the PlantVillage dataset).
- **Disease Segmentation & Severity**: OpenCV HSV-based segmentation highlights diseased regions dynamically and computes disease severity metrics (Mild, Moderate, Severe).
- **Treatment Recommendation Engine**: A rule-based engine providing actionable pesticide and prevention recommendations.
- **History Tracking**: Tracks prior diagnostic results in the session state.

## Project Structure
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

## Setup & Installation

### 1. Backend (FastAPI)
Open a terminal and install dependencies, then start the server:
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
*The backend API will start at `http://localhost:8000`*

### 2. Frontend (Streamlit)
Open a separate terminal, install dependencies, and run the Streamlit app:
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```
*The Streamlit UI will open at `http://localhost:8501`*

## Deep Learning Model Weights
> **Note:** Due to size constraints, the `.pth` weights file for the MobileNetV2 model is not included by default. The system has a fallback "mock" mode allowing full end-to-end testing of the UI, API, segmentation, and recommendations.
To use your trained weights, place your file at `model_weights/model.pth` and the system will automatically detect and load it.
