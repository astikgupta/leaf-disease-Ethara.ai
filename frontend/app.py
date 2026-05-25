import streamlit as st
import base64
import pandas as pd
from PIL import Image
import io
import datetime
from utils import predict_disease

# Set page configuration
st.set_page_config(
    page_title="AI Plant Disease Diagnostics",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .st-emotion-cache-1wivap2 {
        padding: 2rem 1rem;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .severity-mild { color: #28a745; font-weight: bold; }
    .severity-moderate { color: #ffc107; font-weight: bold; }
    .severity-severe { color: #dc3545; font-weight: bold; }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .info-box {
        background-color: #e9ecef;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #007bff;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State for History
if "history" not in st.session_state:
    st.session_state.history = []

def main():
    # Sidebar
    st.sidebar.title("🌿 Plant Diagnostics")
    menu = ["Dashboard", "History Tracking"]
    choice = st.sidebar.selectbox("Navigation", menu)
    
    if choice == "Dashboard":
        render_dashboard()
    elif choice == "History Tracking":
        render_history()

def render_dashboard():
    st.title("AI Plant Disease Diagnostics System")
    st.markdown("Upload a photo of a plant leaf or capture one using your camera to diagnose diseases, analyze severity, and get treatment recommendations.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Image Input")
        input_method = st.radio("Choose Input Method", ["Upload Image", "Camera Capture"])
        
        image_file = None
        if input_method == "Upload Image":
            image_file = st.file_uploader("Upload Leaf Image", type=["jpg", "jpeg", "png"])
        else:
            image_file = st.camera_input("Capture Leaf Image")
            
        if image_file is not None:
            # Display uploaded image
            img = Image.open(image_file)
            st.image(img, caption="Original Image", use_column_width=True)
            
            if st.button("Diagnose Disease", type="primary"):
                with st.spinner("Analyzing image using MobileNetV2 and OpenCV..."):
                    # Process prediction
                    image_bytes = image_file.getvalue()
                    result = predict_disease(image_bytes)
                    
                    if result.get("success"):
                        st.session_state.current_result = result
                        
                        # Add to history
                        record = {
                            "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "Disease": result["prediction"],
                            "Confidence": f"{result['confidence']*100:.1f}%",
                            "Severity": result["severity"]["label"]
                        }
                        st.session_state.history.append(record)
                    else:
                        st.error(f"Error connecting to backend: {result.get('error', 'Unknown Error')}. Ensure FastAPI is running.")
                        
    with col2:
        st.subheader("Diagnostic Results")
        if "current_result" in st.session_state:
            res = st.session_state.current_result
            
            # Overview Metrics
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"<div class='metric-card'><h3>Disease Detected</h3><p style='font-size: 20px; font-weight: bold; color: #e74c3c;'>{res['prediction'].replace('___', ' ').replace('_', ' ')}</p></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div class='metric-card'><h3>Confidence</h3><p style='font-size: 20px; font-weight: bold; color: #3498db;'>{res['confidence']*100:.2f}%</p></div>", unsafe_allow_html=True)
                
            # Severity Section
            st.markdown("---")
            st.subheader("Severity Analysis")
            severity = res["severity"]
            sev_class = severity['label'].lower()
            
            st.markdown(f"**Severity Level:** <span class='severity-{sev_class}'>{severity['label']}</span> ({severity['percentage']}%)", unsafe_allow_html=True)
            st.progress(int(severity['percentage']))
            
            # Segmentation Visual
            st.markdown("---")
            st.subheader("Disease Segmentation")
            st.markdown("HSV-based OpenCV segmentation highlighting the diseased regions.")
            img_data = base64.b64decode(res["segmented_image_base64"])
            segmented_img = Image.open(io.BytesIO(img_data))
            st.image(segmented_img, caption="Segmented Overlay", use_column_width=True)
            
            # Recommendation Engine
            st.markdown("---")
            st.subheader("Treatment Recommendations")
            rec = res["recommendation"]
            
            st.markdown(f"""
            <div class='info-box'>
                <b>Description:</b> {rec['description']}<br><br>
                <b>Recommended Pesticide:</b> {rec['pesticide']}<br>
                <b>Dosage:</b> {rec['dosage']}<br><br>
                <b>Prevention Tips:</b> {rec['prevention']}
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.info("Upload an image and click 'Diagnose Disease' to see results here.")

def render_history():
    st.title("Disease History Tracking")
    if len(st.session_state.history) > 0:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True)
        
        # Simple stats
        st.subheader("Summary Statistics")
        st.bar_chart(df['Disease'].value_counts())
    else:
        st.info("No history available yet. Perform some diagnoses in the dashboard.")

if __name__ == "__main__":
    main()
