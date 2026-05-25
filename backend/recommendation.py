# Rule-based treatment recommendation engine

TREATMENT_DB = {
    "Apple___Apple_scab": {
        "description": "Apple scab is a disease of Malus trees, such as apple trees, caused by the ascomycete fungus Venturia inaequalis.",
        "Mild": {
            "pesticide": "Neem Oil Extract",
            "dosage": "2 ml per liter of water",
            "prevention": "Prune trees to allow better air circulation. Rake and destroy fallen leaves."
        },
        "Moderate": {
            "pesticide": "Captan 50 WP",
            "dosage": "2 grams per liter of water",
            "prevention": "Apply fungicide early in the season. Ensure proper spacing between trees."
        },
        "Severe": {
            "pesticide": "Myclobutanil",
            "dosage": "Follow manufacturer instructions strictly (e.g., 1.5 ml/L)",
            "prevention": "Remove severely infected branches. Consistent fungicide application schedule required."
        }
    },
    "Potato___Early_blight": {
        "description": "Early blight is a common disease of potatoes caused by the fungus Alternaria solani.",
        "Mild": {
            "pesticide": "Copper Fungicide",
            "dosage": "3 grams per liter of water",
            "prevention": "Practice crop rotation. Provide adequate plant spacing."
        },
        "Moderate": {
            "pesticide": "Chlorothalonil",
            "dosage": "2 ml per liter of water",
            "prevention": "Avoid overhead watering. Apply mulch to prevent soil splashing."
        },
        "Severe": {
            "pesticide": "Mancozeb",
            "dosage": "2.5 grams per liter of water",
            "prevention": "Remove infected plant debris immediately. Apply systematic fungicides."
        }
    },
    "Tomato___Late_blight": {
        "description": "Late blight is a potentially devastating disease of tomato and potato, caused by the water mold Phytophthora infestans.",
        "Mild": {
            "pesticide": "Copper Fungicide",
            "dosage": "3 grams per liter of water",
            "prevention": "Water at the base of the plant. Ensure good air flow."
        },
        "Moderate": {
            "pesticide": "Chlorothalonil",
            "dosage": "2 ml per liter of water",
            "prevention": "Remove infected lower leaves. Apply fungicide preemptively in wet weather."
        },
        "Severe": {
            "pesticide": "Mefenoxam or Mancozeb",
            "dosage": "Follow manufacturer labels for severe outbreaks",
            "prevention": "Completely remove and destroy severely infected plants. Do not compost."
        }
    }
}

def get_recommendation(disease_class, severity_label):
    """
    Predict disease severity level to treatment plan.
    Provides Pesticide name, Dosage, Prevention tips.
    """
    if "healthy" in disease_class.lower():
        return {
            "disease_name": disease_class,
            "description": "The plant appears healthy.",
            "pesticide": "None",
            "dosage": "N/A",
            "prevention": "Continue standard care routines (adequate water, sunlight, and fertilizer)."
        }
        
    disease_info = TREATMENT_DB.get(disease_class, None)
    if not disease_info:
        # Generic fallback
        return {
            "disease_name": disease_class,
            "description": "A plant disease was detected, but specific details are not in the current database.",
            "pesticide": "General Broad-Spectrum Fungicide",
            "dosage": "Refer to product packaging based on severity.",
            "prevention": "Isolate the plant, remove heavily infected leaves, and ensure good air circulation."
        }
        
    treatment = disease_info.get(severity_label, disease_info["Moderate"]) # default to moderate if missing
    
    return {
        "disease_name": disease_class,
        "description": disease_info["description"],
        "pesticide": treatment["pesticide"],
        "dosage": treatment["dosage"],
        "prevention": treatment["prevention"]
    }
