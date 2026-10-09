from pathlib import Path

import cv2
import matplotlib.pyplot as plt


# Lokasi file input dan folder output
BASE_DIR = Path(__file__).parent
INPUT_PATH = BASE_DIR / "assets" / "sample.jpg"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


# Membaca gambar dengan OpenCV
image_bgr = cv2.imread(str(INPUT_PATH))

if image_bgr is None:
    raise FileNotFoundError(f"Gambar tidak ditemukan: {INPUT_PATH}")


# OpenCV membaca gambar dalam format BGR.
# Matplotlib membutuhkan format RGB.
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)


# 1. Menyimpan salinan gambar
cv2.imwrite(str(OUTPUT_DIR / "copy.jpg"), image_bgr)


# 2. Resize gambar
resized_image = cv2.resize(image_bgr, (500, 500))
cv2.imwrite(str(OUTPUT_DIR / "resized.jpg"), resized_image)


# 3. Crop gambar
height, width = image_bgr.shape[:2]

crop_image = image_bgr[
    height // 4 : height * 3 // 4,
    width // 4 : width * 3 // 4
]

cv2.imwrite(str(OUTPUT_DIR / "cropped.jpg"), crop_image)


# 4. Mengubah gambar menjadi grayscale
gray_image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
cv2.imwrite(str(OUTPUT_DIR / "gray.jpg"), gray_image)


# Menampilkan informasi gambar
print("Nama file:", INPUT_PATH.name)
print("Ukuran gambar:", width, "x", height)
print("Jumlah channel:", image_bgr.shape[2])
print("File hasil disimpan di:", OUTPUT_DIR)


# Menampilkan beberapa hasil sekaligus
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("Original")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.title("Resized")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(crop_image, cv2.COLOR_BGR2RGB))
plt.title("Cropped")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.tight_layout()
plt.show()