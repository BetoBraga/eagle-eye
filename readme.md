Object Detection with Detectron2 and Streamlit
==============================================

This repository contains a simple **Streamlit** application that uses **Detectron2** to perform object detection on images. You can upload an image (PNG, JPG, or JPEG), and the app processes the image using a pre-trained COCO model to display and allow you to download the annotated image (with bounding boxes and class labels).

Application Overview
--------------------

1.  **Image Upload**  
    The user selects a local image to upload.
2.  **Processing**  
    The application uses a pre-trained instance segmentation model from Detectron2 (`COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml`) to detect objects.
3.  **Visualization**  
    The resulting image, annotated with bounding boxes and labels, is displayed on the Streamlit page.
4.  **Download**  
    A button allows you to download the annotated image as a PNG file.

Project Structure
-----------------
<br>
├── app.py            (Main Streamlit application code) <br>
├── Dockerfile        (Optional Dockerfile to build an image with Detectron2 and Streamlit) <br>
└── README.md         (This documentation file <br>

Prerequisites
-------------

*   Python 3.8+
*   pip for installing dependencies

Installation
------------

1.  Clone the repository (or download the files).

    ```git clone https://github.com/BetoBraga/eagle-eye```
2.  Install the dependencies:
    
    ```pip install streamlit opencv-python-headless pillow```
    
    Then, install Detectron2 (CPU version) as per the official instructions or by using:
    
    pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.8/index.html
    

Running Locally
---------------

1.  Open a terminal in the directory containing `app.py`.
2.  Run Streamlit:
    
    ```streamlit run app.py```
    
3.  Access the application:  
    The terminal will display a link (usually `http://localhost:8501`). Open it in your browser to use the app.

Usage
-----

1.  **Upload an Image**  
    Click the button to upload a PNG, JPG, or JPEG file.
2.  **View the Results**  
    The app displays the processed image with detected objects (bounding boxes and labels).
3.  **Download the Annotated Image**  
    Click the "Download Annotated Image" button to save the result locally as a PNG file.

Running via Docker (Optional)
-----------------------------

1.  **Build the Docker image:**
    
    docker build -t detectron2-streamlit .
    
2.  **Run the container:**
    
    docker run -p 8501:8501 --rm detectron2-streamlit
    
3.  **Access the application:**  
    Open `http://localhost:8501` in your browser.

**Note:** If you want to mount a volume to exchange files (e.g., for input/output images), use the `-v` option with the `docker run` command.

Credits
-------

*   **Detectron2** – Object detection framework developed by Facebook AI Research.
*   **Streamlit** – A tool for rapidly building web apps in Python.