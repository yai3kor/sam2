import os
from PIL import Image

input_dir = "/media/RTCIN15TB/AllUsers/ALLIANCE-DC01-IMU_LBXR268-D-002_20240112_111253"
output_dir = "/media/RTCIN9TBA/Interns/RDT2/yai3kor/workspace/sam2/notebooks/videos/road"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path).convert("RGB")
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        img.save(os.path.join(output_dir, jpg_filename), "JPEG")
