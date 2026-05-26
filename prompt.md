AI Plant Disease Diagnostics System

Prompt

Context and Role
I create computer vision and intelligent farming systems. I am hired to develop a website. This website assists users in diagnosing diseases that their plants may suffer from.
This website does the following:
It analyses photos of leaves
It diagnoses the disease affecting the plant
It diagnoses the extent to which the plant is diseased
It provides recommendations for treating the plant
It should be noted that this website should be easily accessible and user-friendly both on mobile phones and computers.
Users do the following actions:
They upload photos of leaves
They receive their diagnosis and recommendations
The website uses algorithms and software. Algorithms analyse uploaded photos. Then, they diagnose the problems. After diagnosing the disease, they provide necessary recommendations. Such recommendations are supposed to solve users' problems.
This website does the following:
It diagnoses the disease affecting the leaf
It provides guidelines for eliminating the disease

Objective
This project is about making a website that can help people find out what is wrong with a plant leaf. The website is simple to use. It uses special computer methods to look at pictures of leaves and figure out what disease they have. People can upload pictures of leaves. Take new ones and the website will tell them what is wrong with the leaf. It uses something called MobileNetV2 to do this. It also tells people how sure it is about the answer.
The website can also look at the picture of the leaf. Figure out how bad the disease is. It can say if the disease is Mild or Moderate or really bad which is called Severe. Then it tells people what they can do to make the plant better like what kind of medicine to use on it and how to stop the disease from happening.
This website is made with something called Streamlit. It is designed to be easy to use on computers and phones. It is for farmers and anyone else who wants to know what is wrong with their plants.

Farmer-Friendly Clarification
This application requires no login or registration. It is designed for farmers with limited technical knowledge. All features must be accessible without any account creation.

Frontend & UI Requirements
Framework
To use: Streamlit for frontend.
Streamlit is chosen because it is a Python-based framework that makes it very easy and fast to build interactive web applications without needing separate frontend coding. Since our entire backend and AI pipeline is in Python, Streamlit keeps everything in one language and makes deployment simple. It is also easy to use on both mobile and desktop, which is important for farmers who may not have powerful devices.
UI Features
The interface should include:
Dashboard
Image upload
Camera capture
Segmentation visualization
Severity analysis section
Disease information section
Treatment recommendation section
Disease history tracking
The UI should be:
Responsive
Easy to use
Modern look

Backend Requirements
Implement backend functionality for:
Loading the trained model securely
Handling prediction requests
Returning formatted JSON output
Logging of prediction history
Handle both uploaded images and camera-captured images as input for prediction pipeline
Disease history must be stored in the current browser session only — no database or user account required
FastAPI is used as the backend framework because it is very fast, lightweight, and works perfectly with Python-based AI and machine learning models. It handles multiple requests at the same time without slowing down, which is important when farmers are uploading images and waiting for quick results. It also makes it easy to return clean JSON responses to the frontend.

AI & Computer Vision Requirements
Disease Classification
Implement a deep learning algorithm:
MobileNetV2
Transfer learning technique
PlantVillage dataset from Kaggle
MobileNetV2 is selected because it is a lightweight model that runs fast even on basic devices. Since farmers may not have powerful computers or phones, this model is a perfect fit. Transfer learning saves time by using knowledge the model already has and fine-tuning it for plant diseases.
This deep learning algorithm should be able to:
Determine disease label
Output confidence score
Maintain accuracy of classification
Image Preprocessing
Implement image preprocessing pipeline, which includes:
RGB conversion
Image resize (224×224)
Normalization
Optimize image preprocessing for efficient CNN inference.
Disease Segmentation
Implement HSV-based image segmentation using OpenCV to:
Identify diseased regions
Isolate healthy from diseased pixels
Create overlay masks for diseases
Locate diseased regions visually
Apply morphological operations for noise elimination
OpenCV with HSV color segmentation is used because plant diseases usually show up as specific colors on leaves — like yellow spots, brown patches, or dark marks. HSV color space makes it much easier to detect these color-based differences compared to regular RGB. OpenCV is a powerful and fast image processing library that can handle this in real time without slowing down the application.
Severity Measurement
Calculate severity ratio using:
Severity % = (Diseased Pixels / Total Leaf Pixels) × 100
Classify severity into:
Mild (0–25%)
Moderate (25–60%)
Severe (>60%)
Display severity visually using:
Progress bars
Color indicators
Treatment Recommendation Engine
Implement a rule-based recommendation engine that:
Predicts disease + severity to recommend treatment
Provides:
Pesticide name
Dosage
Prevention tips

Output Requirements
The expected outcomes of the developed system will include:
Disease diagnosis with confidence level provided
Image segmentation of leaf with disease areas marked out
Severity status provided — Mild / Moderate / Severe
Recommendations with pesticide used, dose, and preventive measures
History of diseases within the current session
Appropriate error message handling with bad input handling
Working on all types of devices — mobile and desktop

Model Training Configuration
Describe the model training process to include:
Pre-trained MobileNetV2 weights usage
Approach of transfer learning
Split of training and validation datasets (80/20)
Optimizer: Adam
Loss Function: Cross Entropy Loss
Batch size and epoch setup
Fine-tuning method for fine-tuning the model
Model saving and loading
Your model should have the capability to:
Use pre-trained MobileNetV2 fine-tuned on PlantVillage
Fine-tune your pre-trained model (recommended)

Data for Treatment Recommendations
Design a structure for diseases and their recommended treatments as:
Name of disease
Recommended pesticide / fungicide
Dosage guidelines
Frequency of application
Preventive measures
Different treatment for different levels of severity of disease
The recommendation algorithm shall be based on rule-based mappings.

Performance and Scalability
Optimize:
Inference time for model
UI reactivity
Lazy loading of heavy modules
Optimized OpenCV processing
Achieve:
Real-time predictions
Low latency
Scalability

Error Handling and Documentation
Error Handling
Handle both the frontend and backend errors effectively for enhanced functionality and performance.
Frontend Error Handling
Handle error with invalid image upload
Display appropriate message when uploading unsupported file formats
Display a loader when predicting the output
Display appropriate message when the prediction is not done correctly
Prevent submitting empty forms
Backend Error Handling
Validating the uploaded image safely
Handling exceptions in preprocessing and model prediction
Sending an appropriate response in case of failure and success
Logging all errors from the backend to debug issues
Model loading and segmentation exception handling

Technology Stack
Frontend
Streamlit
AI/ML
PyTorch — chosen because it is the most flexible and researcher-friendly deep learning framework. It works very naturally with MobileNetV2 through Torchvision, and makes model loading, fine-tuning, and inference straightforward. PyTorch is also widely used in production AI systems, making it a reliable and future-proof choice.
Torchvision
MobileNetV2
Computer Vision
OpenCV
Pillow
NumPy
Backend
Python
FastAPI
Data Handling
Pandas

