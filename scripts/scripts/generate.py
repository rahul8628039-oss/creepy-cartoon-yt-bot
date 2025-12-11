from PIL import Image, ImageDraw
import os, random

os.makedirs("outputs/frames", exist_ok=True)

def generate_frames():
    for i in range(12):
        img = Image.new("RGB", (1080, 1920), "black")
        d = ImageDraw.Draw(img)
        d.text((200, 900), f"Creepy Frame {i+1}", fill="red")
        img.save(f"outputs/frames/frame_{i}.png")

if __name__ == "__main__":
    generate_frames()
