# ShadowClone AI 🥷

**ShadowClone AI** is a real-time computer vision application that brings the iconic "Shadow Clone Jutsu" to life! Built with Python, it utilizes advanced AI models to detect hand signs and seamlessly project opaque clones of yourself in the background.

## 🌟 Features
- **🖐️ Hand Sign Activation:** Powered by **MediaPipe**, the effect only activates when you bring your index fingers together (like a Jutsu hand sign!).
- **👤 Real-time Segmentation:** Uses **YOLOv8** (`yolov8n-seg`) to accurately cut out your silhouette from the background in real-time.
- **🌌 Z-Index Depth Control:** Smart depth ordering ensures that your original body stays perfectly in the foreground while the clones remain behind you.

## 🛠️ Tech Stack
- **OpenCV:** For real-time video capture and image processing.
- **MediaPipe:** For precise hand tracking and landmark detection.
- **YOLOv8 (Ultralytics):** For high-speed instance segmentation.
- **NumPy:** For advanced matrix transformations and mask handling.

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/owaiskhan2501000/ShadowClone_AI.git
cd ShadowClone_AI
```

### 2. Install Dependencies
Make sure you have Python installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```
*(Note: The `yolov8n-seg.pt` model will automatically download the first time you run the script.)*

## 🎮 How to Use
1. Run the script and stand in front of your webcam.
2. Bring your two index fingers close together.
3. Watch the **Ultimate Opaque Shadow Clones** appear right behind you!
4. Press `q` to exit the application.

---
*Created by [Owais Khan](https://github.com/owaiskhan2501000)*