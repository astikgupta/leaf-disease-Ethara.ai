import cv2
import numpy as np

def segment_and_calculate_severity(image_np):
    """
    Apply HSV based image segmentation using OpenCV to find diseased areas.
    Calculate severity ratio.
    Returns: (severity_percentage, severity_label, segmented_image_bgr)
    """
    # Convert RGB (expected input) to HSV
    hsv = cv2.cvtColor(image_np, cv2.COLOR_RGB2HSV)
    
    # Define color range for healthy green leaves
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([95, 255, 255])
    
    # Define mask for green (healthy parts)
    healthy_mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Background thresholding (to isolate the leaf from the background)
    # Assuming background is generally very dark, very bright or white
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    _, leaf_mask = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    
    # Morphological operations for noise elimination on leaf_mask
    kernel = np.ones((5, 5), np.uint8)
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_CLOSE, kernel)
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_OPEN, kernel)
    
    # Diseased mask is the leaf area that is NOT healthy green
    diseased_mask = cv2.bitwise_and(leaf_mask, cv2.bitwise_not(healthy_mask))
    
    # Morphological clean up on diseased mask
    diseased_mask = cv2.morphologyEx(diseased_mask, cv2.MORPH_OPEN, kernel)
    
    # Calculate Severity
    total_leaf_pixels = cv2.countNonZero(leaf_mask)
    diseased_pixels = cv2.countNonZero(diseased_mask)
    
    severity_percentage = 0.0
    if total_leaf_pixels > 0:
        severity_percentage = (diseased_pixels / total_leaf_pixels) * 100

    # Severity Label Classification
    if severity_percentage < 25:
        severity_label = "Mild"
    elif severity_percentage < 60:
        severity_label = "Moderate"
    else:
        severity_label = "Severe"
        
    # Create overlay mask for diseases visually (red overlay on diseased parts)
    segmented_img = image_np.copy()
    
    # Highlight diseased areas with red
    segmented_img[diseased_mask > 0] = [255, 0, 0] # RGB Red
    
    # Convert back to BGR for standard OpenCV handling if needed later, 
    # but since we output for PIL/web, we can keep it RGB or convert to BGR for base64 encoding later
    return severity_percentage, severity_label, segmented_img
