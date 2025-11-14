# Q8 - YOLO Object Detection (Ashish Pawar, 23I5120)
from ultralytics import YOLO
import os

student_name = "Ashish Pawar"
roll_number = "23I5120"
print("Student Name:", student_name)
print("Roll Number:", roll_number)

# Local image - place 'football.jpg' in the same folder
image_path = "football.jpg"
model = YOLO("yolov8n.pt")

results = model.predict(source=image_path, save=True)
output_path = os.path.join(results[0].save_dir, os.path.basename(image_path))
print("\nAnnotated image saved at:", output_path, "\n")

# Print detected classes and confidence
class_names = model.names
print("Detected Objects:")
for box in results[0].boxes:
    cls = int(box.cls[0])
    conf = float(box.conf[0])
    print(f"{class_names[cls]}  |  Confidence: {conf:.2f}")
