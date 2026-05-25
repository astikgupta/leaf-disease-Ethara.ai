import requests
import io

API_URL = "http://localhost:8000/predict"

def predict_disease(image_file):
    """
    Send image to FastAPI backend and get prediction results.
    """
    try:
        files = {"file": ("image.jpg", image_file, "image/jpeg")}
        response = requests.post(API_URL, files=files)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}
