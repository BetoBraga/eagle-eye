# app.py

# Monkey patch PIL.Image before any other imports
from PIL import Image
if not hasattr(Image, "LINEAR"):
    Image.LINEAR = Image.BILINEAR

import streamlit as st
import cv2
import numpy as np

# Import Detectron2 modules after the monkey patch
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import Visualizer, ColorMode

def setup_model():
    cfg = get_cfg()
    cfg.merge_from_file(
        model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
    )
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # Confidence threshold
    cfg.MODEL.DEVICE = "cpu"  # Force CPU usage
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(
        "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
    )
    predictor = DefaultPredictor(cfg)
    metadata = MetadataCatalog.get("coco_2017_val")
    return predictor, metadata

def detect_objects(image, predictor, metadata):
    outputs = predictor(image)
    visualizer = Visualizer(image[:, :, ::-1], metadata=metadata, scale=1.0, instance_mode=ColorMode.IMAGE)
    out = visualizer.draw_instance_predictions(outputs["instances"].to("cpu"))
    result = out.get_image()[:, :, ::-1]
    return result

def main():
    st.title("Project EagleEye: Object Detection")
    
    # File uploader waits for user input
    uploaded_file = st.file_uploader("Upload an image (PNG, JPG, or JPEG)", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        # Load the model only after a file is uploaded
        predictor, metadata = setup_model()
        
        # Convert the uploaded file to an OpenCV image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        if image is None:
            st.error("Error loading the image.")
            return
        
        # Run object detection on the image
        result = detect_objects(image, predictor, metadata)
        
        # Display the processed image
        st.image(result, channels="BGR", caption="Detected Objects")
        
        # Create a download button for the processed image
        _, buffer = cv2.imencode(".png", result)
        st.download_button(
            "Download Annotated Image",
            buffer.tobytes(),
            file_name="output.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
