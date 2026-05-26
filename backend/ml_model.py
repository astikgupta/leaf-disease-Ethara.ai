import torch
import torchvision.models as models
from torchvision.transforms import functional as F
import os
import random

# For demonstration, we simulate the classes. 
# PlantVillage has 38 classes, we use a smaller subset for demonstration.
CLASSES = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___healthy",
    "Potato___Early_blight", "Potato___Late_blight", "Potato___healthy",
    "Tomato___Early_blight", "Tomato___Late_blight", "Tomato___healthy"
]

class PlantDiseaseModel:
    def __init__(self, model_path="model_weights/model.pth"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_path = model_path
        self.model = models.mobilenet_v2(pretrained=False)
        self.model.classifier[1] = torch.nn.Linear(self.model.last_channel, len(CLASSES))
        
        self.is_mock = False
        try:
            if os.path.exists(self.model_path):
                self.model.load_state_dict(torch.load(self.model_path, map_location=self.device))
                self.model.to(self.device)
                self.model.eval()
            else:
                print(f"Warning: Model weights not found at {self.model_path}. Using mock mode.")
                self.is_mock = True
        except Exception as e:
            print(f"Error loading model: {e}. Using mock mode.")
            self.is_mock = True

    def predict(self, image_tensor):
        """
        Predict disease from preprocessed image tensor.
        Returns: (predicted_class_name, confidence_score)
        """
        if self.is_mock:
            # Mock prediction logic if model is not loaded
            pred_idx = random.randint(0, len(CLASSES) - 1)
            confidence = random.uniform(0.6, 0.99)
            return CLASSES[pred_idx], confidence

        image_tensor = image_tensor.to(self.device)
        with torch.no_grad():
            outputs = self.model(image_tensor)
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
            confidence, predicted_idx = torch.max(probabilities, 0)
        
        return CLASSES[predicted_idx.item()], confidence.item()

# Global instance
model_instance = PlantDiseaseModel()

def get_prediction(image_tensor):
    return model_instance.predict(image_tensor)
