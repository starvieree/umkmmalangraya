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
    "hero-bakso-malang.jpg", "hero-keripik-tempe-sanan.jpg", "hero-batik-malangan.jpg",
    "kategori-kuliner.jpg", "kategori-kriya.jpg", "kategori-fashion.jpg",
    "kategori-kebun.jpg", "kategori-jasa.jpg", "produk-bakso-arema-klojen.jpg",
    "produk-keripik-tempe-bu-siti.jpg", "produk-keramik-dinoyo-sari.jpg",
    "produk-batik-malangan-ratri.jpg", "blog-menyusuri-sanan-kampung-keripik-tempe.jpg",
    "blog-bazar-umkm-akhir-pekan-di-batu.jpg", "blog-tips-foto-produk-pakai-hp.jpg",
    "tentang-lapak-umkm-bazar.jpg", "produk-apel-batu-pak-darmo.jpg",
    "produk-susu-murni-pujon.jpg", "produk-servis-kulkas-blimbing.jpg",
    "produk-kopi-dampit-kedung.jpg", "blog-kopi-robusta-dampit-di-cangkir-lokal.jpg"
]

for img_name in images:
    input_path = os.path.join(img_dir, img_name)
    if os.path.exists(input_path):
        output_name = os.path.splitext(img_name)[0] + ".webp"
        output_path = os.path.join(img_dir, output_name)
        compress_and_convert(input_path, output_path)
    else:
        print(f"File not found: {input_path}")
