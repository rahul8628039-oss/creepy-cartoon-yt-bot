from PIL import Image, ImageDraw

img = Image.new("RGB", (1280, 720), "black")
d = ImageDraw.Draw(img)
d.text((300, 300), "CREEPY CARTOON", fill="red")
img.save("outputs/thumbnail.jpg")
