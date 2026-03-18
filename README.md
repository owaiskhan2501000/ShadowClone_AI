# Shadow Clone AI (Jutsu Hand Sign Recognition)

This is a Computer Vision project that uses OpenCV, MediaPipe, and YOLOv8 to create a real-time "Shadow Clone" visual effect triggered by a specific hand sign (inspired by Naruto).

## Features
* **Real-time Hand Tracking:** Uses MediaPipe to detect the exact hand pose.
* **Gesture Recognition:** Custom logic to recognize the "Cross" index finger gesture.
* **Body Segmentation:** Uses YOLOv8 Nano (`yolov8n-seg.pt`) to precisely cut out the user's body from the background.
* **VFX Compositing:** Uses OpenCV's affine transformations and alpha blending to create opaque, depth-aware clones with a smoke puff entrance effect.

## How to Run
1. Install the required libraries:
   `pip install opencv-python mediapipe ultralytics numpy`
2. Run the script:
   `python main.py`
3. Ensure your webcam or DroidCam is connected. Make the "Cross" hand sign to activate the jutsu!

## Developer
Developed by Mohammad Owais.
