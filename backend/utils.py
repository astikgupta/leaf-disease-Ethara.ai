import io
from PIL import Image
import numpy as np
import torchvision.transforms as transforms

def preprocess_image(image_bytes):
    """
    Implement image preprocessing pipeline:
    - Conversion to RGB mode
    - Resizing image (224x224)
    - Normalization for MobileNetV2
    Returns:
    - numpy array of the image (for OpenCV segmentation)
    - torch tensor (for PyTorch MobileNetV2 inference)
    """
    # Load image from bytes
    image = Image.open(io.BytesIO(image_bytes))
    
    # Conversion to RGB mode
    if image.mode != "RGB":
        image = image.convert("RGB")
        
    # Keep a numpy copy for OpenCV before deep learning transforms
    image_np = np.array(image)
    
    # Define transformations for MobileNetV2
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    # Apply transformation
    image_tensor = transform(image).unsqueeze(0) # Add batch dimension
    
    return image_np, image_tensor
