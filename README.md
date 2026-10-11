# Direktori UMKM Malang Raya (multi-halaman)

18 file HTML statis, tanpa build step.

- index, tentang, kategori, katalog, blog, gabung  (6 halaman utama)
- katalog/*.html  (8 detail UMKM)
- blog/*.html     (4 detail artikel)
- css/style.css, js/site.js, robots.txt, sitemap.xml, .htaccess, img/

Jalankan: buka index.html, atau `python3 -m http.server 8000`.
Sebelum live: ganti domain umkmmalang.id, nomor WA, data contoh, dan isi img/ (og-image.jpg, logo.png, foto asli).
Canonical memakai URL tanpa .html; gunakan hosting dengan clean URL (Netlify/Vercel/Cloudflare Pages) atau .htaccess bawaan.
