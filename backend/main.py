from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
import base64
import cv2
import time

from .utils import preprocess_image
from .ml_model import get_prediction
from .segmentation import segment_and_calculate_severity
from .recommendation import get_recommendation

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("backend/logs/app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Plant Disease Diagnostics API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Plant Disease Diagnostics API"}

@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    start_time = time.time()
    logger.info(f"Received prediction request for file: {file.filename}")
    
    if not file.content_type.startswith("image/"):
        logger.error(f"Invalid file type uploaded: {file.content_type}")
        raise HTTPException(status_code=400, detail="File must be an image.")
    
    try:
        # Read image
        image_bytes = await file.read()
        
        # Preprocess
        image_np, image_tensor = preprocess_image(image_bytes)
        
        # Predict Class
        predicted_class, confidence = get_prediction(image_tensor)
        logger.info(f"Predicted class: {predicted_class} with confidence: {confidence:.2f}")
        
        # Segment and calculate severity
        severity_percentage, severity_label, segmented_img = segment_and_calculate_severity(image_np)
        
        # Get Recommendation
        recommendation = get_recommendation(predicted_class, severity_label)
        
        # Convert segmented image to base64 for frontend
        # OpenCV uses BGR, image_np was RGB, we made segmented_img as RGB-like but lets encode it
        # Actually segmented_img is currently RGB, we need to convert to BGR for cv2.imencode
        segmented_bgr = cv2.cvtColor(segmented_img, cv2.COLOR_RGB2BGR)
        _, buffer = cv2.imencode('.png', segmented_bgr)
        segmented_base64 = base64.b64encode(buffer).decode('utf-8')
        
        inference_time = time.time() - start_time
        logger.info(f"Prediction successful in {inference_time:.2f}s")
        
        return {
            "success": True,
            "prediction": predicted_class,
            "confidence": confidence,
            "severity": {
                "percentage": round(severity_percentage, 2),
                "label": severity_label
            },
            "recommendation": recommendation,
            "segmented_image_base64": segmented_base64,
            "inference_time_seconds": round(inference_time, 2)
        }
        
    except Exception as e:
        logger.exception("Error during prediction process")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

