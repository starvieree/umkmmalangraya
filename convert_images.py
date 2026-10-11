import os
from PIL import Image

def compress_and_convert(image_path, output_path, max_size_kb=75):
    img = Image.open(image_path)
    quality = 90
    while quality > 5:
        img.save(output_path, "WEBP", quality=quality)
        if os.path.getsize(output_path) <= max_size_kb * 1024:
            break
        quality -= 5
    print(f"Converted {image_path} to {output_path} (Size: {os.path.getsize(output_path)/1024:.2f} KB)")

img_dir = "img"
images = [
    "logo.jpg"
]

for img_name in images:
    input_path = os.path.join(img_dir, img_name)
    if os.path.exists(input_path):
        output_name = os.path.splitext(img_name)[0] + ".webp"
        output_path = os.path.join(img_dir, output_name)
        compress_and_convert(input_path, output_path)
    else:
        print(f"File not found: {input_path}")
