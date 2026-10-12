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
    "katalog-keripik-tempe-bu-siti-toko.jpg",
    "katalog-keripik-tempe-bu-siti-logo.jpg",
    "katalog-keripik-tempe-bu-siti-original-250gr.jpg",
    "katalog-keripik-tempe-bu-siti-jeruk-purut-250gr.jpg",
    "katalog-keripik-tempe-bu-siti-paket-oleh-oleh.jpg",
    "katalog-kopi-dampit-kedung-toko.jpg",
    "katalog-kopi-dampit-kedung-logo.jpg",
    "katalog-kopi-dampit-kedung-biji-robusta-250gr.jpg",
    "katalog-kopi-dampit-kedung-kopi-susu-gula-aren.jpg",
    "katalog-kopi-dampit-kedung-drip-bag-10.jpg",
    "katalog-servis-kulkas-blimbing-toko.jpg",
    "katalog-servis-kulkas-blimbing-logo.jpg",
    "katalog-servis-kulkas-blimbing-cek-diagnosa.jpg",
    "katalog-servis-kulkas-blimbing-cuci-ac.jpg",
    "katalog-servis-kulkas-blimbing-servis-mesin-cuci.jpg",
    "katalog-susu-murni-pujon-toko.jpg",
    "katalog-susu-murni-pujon-logo.jpg",
    "katalog-susu-murni-pujon-susu-murni-1-liter.jpg",
    "katalog-susu-murni-pujon-yogurt-plain-250ml.jpg",
    "katalog-susu-murni-pujon-yogurt-stroberi-250ml.jpg",
]

for img_name in images:
    input_path = os.path.join(img_dir, img_name)
    if os.path.exists(input_path):
        output_name = os.path.splitext(img_name)[0] + ".webp"
        output_path = os.path.join(img_dir, output_name)
        compress_and_convert(input_path, output_path)
    else:
        print(f"File not found: {input_path}")
