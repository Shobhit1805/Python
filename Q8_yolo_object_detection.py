# Q8 - Object Detection using YOLO model
# Replace with your own details before submission

from ultralytics import YOLO
import cv2

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q8 - Object Detection using YOLO\n")

# Step 1: Load pre-trained YOLOv8 model
model = YOLO('yolov8n.pt')  # 'n' = nano version (fast & lightweight)

# Step 2: Read the image file
image_path = "car.png"  # <-- change this to your image name
img = cv2.imread(image_path)

if img is None:
    print("❌ Image not found! Place your image in the same folder.")
else:
    # Step 3: Run YOLO inference (object detection)
    results = model.predict(source=image_path, save=True)

    print("✅ Object Detection Completed Successfully!")
    print("Detected Objects Summary:\n", results[0].boxes.data)

    print("\nDetected image saved inside the 'runs/detect/predict' folder.")
