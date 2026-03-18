import cv2
import mediapipe as mp
import math
import numpy as np
from ultralytics import YOLO

# 1. YOLO Model Load Kerna
print("Loading YOLO AI Model...")
yolo_model = YOLO("yolov8n-seg.pt")
print("YOLO Model Loaded Successfully!")

# 2. MediaPipe Hands setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Effect Settings
clone_offset = 200  

while True:
    success, img = cap.read()
    if not success:
        break
    
    img = cv2.flip(img, 1)
    img_clean = img.copy() 
    h, w, c = img.shape
    
    img_rgb = cv2.cvtColor(img_clean, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    jutsu_activated = False

    if results.multi_hand_landmarks:
        if len(results.multi_hand_landmarks) == 2:
            hand1 = results.multi_hand_landmarks[0]
            hand2 = results.multi_hand_landmarks[1]
            
            x1, y1 = int(hand1.landmark[8].x * w), int(hand1.landmark[8].y * h)
            x2, y2 = int(hand2.landmark[8].x * w), int(hand2.landmark[8].y * h)
            
            distance = math.hypot(x2 - x1, y2 - y1)
            
            if distance < 100: 
                jutsu_activated = True
                cv2.circle(img, ((x1+x2)//2, (y1+y2)//2), 20, (0, 255, 0), cv2.FILLED)

        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
    # ---------------------------------------------------
    # ADVANCED PHASE: Depth Ordering (Clones in Background)
    # ---------------------------------------------------
    if jutsu_activated:
        yolo_results = yolo_model(img_clean, classes=[0], verbose=False)
        
        if yolo_results[0].masks is not None:
            mask = yolo_results[0].masks.data[0].cpu().numpy()
            mask = cv2.resize(mask, (w, h))
            
            cutout_clean = np.zeros_like(img_clean)
            cutout_clean[mask > 0.5] = img_clean[mask > 0.5]
            
            matrix_left = np.float32([[1, 0, -clone_offset], [0, 1, 0]])
            left_clone = cv2.warpAffine(cutout_clean, matrix_left, (w, h))
            
            matrix_right = np.float32([[1, 0, clone_offset], [0, 1, 0]])
            right_clone = cv2.warpAffine(cutout_clean, matrix_right, (w, h))
            
            clones_layer_opaque = cv2.add(left_clone, right_clone)
            
            # --- THE FIX: Z-Indexing (Depth Control) ---
            # 1. Pehchan kero ke clones kahan mojood hain?
            clone_condition = np.any(clones_layer_opaque > 0, axis=2)
            
            # 2. Pehchan kero ke tumhari asli body kahan mojood hai?
            original_body_condition = mask > 0.5
            
            # 3. Final Shart: Clones draw karo jahan clones mojood hon LEKIN asli body na ho
            # Numpy me '~' ka matlab 'NOT' hota hai (Yani jahan body nahi hai)
            final_condition = clone_condition & ~original_body_condition
            
            # 4. Asli image par un pixels ko replace kardo
            img[final_condition] = clones_layer_opaque[final_condition]
            
        cv2.putText(img, "ULTIMATE SHADOW CLONES ACTIVATED!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    else:
        cv2.putText(img, "Waiting for Hand Sign...", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
    cv2.imshow("Ultimate Opaque Shadow Clone Project", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()