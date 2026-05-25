# AI-Based Leaf Disease Detection Project Prompt 

## Context and Role

I create computer vision and intelligent farming systems. I am hired to develop a website. This website assists users in diagnosing diseases that their plants may suffer from.

This website does the following:
- it analyses photos of leaves;
- it diagnoses the disease affecting the plant;
- it diagnoses the extent to which the plant is diseased;
- it provides recommendations for treating the plant.

It should be noted that this website should be easily accessible and user-friendly both on mobile phones and computers.

Users do the following actions:
- they upload photos of leaves;
- they receive their diagnosis and recommendations.

The website uses algorithms and software. Algorithms analyse uploaded photos. Then, they diagnose the problems. After diagnosing the disease, they provide necessary recommendations. Such recommendations are supposed to solve users' problems.

This website does the following:
- it diagnoses the disease affecting the leaf;
- it provides guidelines for eliminating the disease.


## Objective

Create an end-to-end AI plant disease diagnostics system that is capable of:
- Recognizing plant diseases using leaf pictures through deep learning.
- Analyzing the severity level and segmenting the diseases.
- Providing intelligent treatment suggestions.
- Producing real-time visual interactive outcomes.
- Exhibiting great responsiveness and production UI/UX.


## Frontend & UI Requirements 

**For the framework:**
- To use: Streamlit for frontend 

**UI Features:**
The interface should include:
- Dashboard
- Image upload 
- Camera capture
- Segmentation visualization
- Severity analysis section
- Disease information section
- Treatment recommendation section
- Disease history tracking 

**The UI should be:**
- Responsive
- Easy of use
- Modern look

## Backend Requirements
Implement backend functionality for:
- Loading the trained model securely 
- Processing the uploaded images
- Handling prediction requests 
- Returning formatted JSON output 
- Logging of prediction history

## AI & Computer Vision Requirements 

**For disease Classification:**
Implement a deep learning algorithm:
- MobileNetV2
- Transfer learning technique
- Plant village dataset from Kaggle

This deep learning algorithm should be able to:
- Determine disease label
- Output Confidence Score
- Maintain accuracy of classification

**Image Preprocessing:**
Implement image preprocessing pipeline, which includes:
- RGB conversion
- Image resize (224×224)
- Normalization

Optimize image preprocessing for efficient CNN inference.

**Disease Segmentation:**
Implement HSV-based image segmentation using OpenCV to:
- Identify diseased regions
- Isolate healthy from diseased pixels
- Create overlay masks for diseases
- Locate diseased regions visually

**Severity Measurement:**
Calculate severity ratio using:
`Severity % = (Diseased Pixels / Total Leaf Pixels) × 100`

Classify severity into:
- Mild (0-25%)
- Moderate (25-60%)
- Severe (>60%)

Display severity visually using: 
- Progress bars
- Color indicators

## Treatment Recommendation Engine 

Develop rule-based treatment recommendation engine that will help in:
- Predicting disease severity level to treatment plant
- Suggests: Pesticide name, Dose

Implement a rule-based recommendation engine that:
- Predict disease + severity to treatment plant 
- Provides: Pesticide name, Dosage, Prevention tips

## Performance and Scalability

**Optimize:**
- Inference time for model
- UI reactivity
- Lazy loading of heavy modules
- Optimized OpenCV processing

**Achieve:**
- Real-time predictions
- Low latency
- Scalability

## Error Handling and Documentation

Handle both the frontend and backend errors effectively for enhanced functionality and performance.

**Frontend Error Handling:**
- Handle error with invalid images upload
- Display appropriate message when uploading unsupported file formats
- Display a loader when predicting the output
- Display appropriate message when the prediction is not done correctly
- Prevent submitting empty forms

**Backend Error Handling:**
- Validating the uploaded image safely
- Handling exceptions in preprocessing and model prediction
- Sending an appropriate response in case of failure and success
- Logging all errors from the backend to debug issues
- Model Loading and Segmentation Exception Handling

## Technology Stack
Use the following:

- **Frontend:** Streamlit
- **AI/ML:** PyTorch, Torchvision, MobileNetV2
- **Computer Vision:** OpenCV, Pillow, NumPy
- **Backend:** Python, FastAPI
- **Data Handling:** Pandas
