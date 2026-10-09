# Project 01 — Color Detection

## Tujuan

Mendeteksi objek berdasarkan warna melalui webcam dan menggambar bounding box pada objek
yang masuk rentang HSV tertentu.

## Level

Beginner

## Estimasi Waktu

2–3 hari

## Materi yang Dipelajari

- BGR, RGB, dan HSV.
- `cv2.inRange()` dan masking.
- Noise sederhana, contour, dan bounding box.
- Deteksi warna real-time melalui webcam.

## Library yang Digunakan

- OpenCV: konversi warna, mask, contour, webcam, dan rectangle.
- NumPy: array warna dan batas HSV.

## Instalasi

```powershell
python -m pip install -r ..\..\requirements.txt
```

## Dokumentasi Resmi

- HSV dan konversi warna: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
- `inRange`: https://docs.opencv.org/4.x/da/d97/tutorial_threshold_inRange.html
- Contour: https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
- Bounding rectangle: https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
- VideoCapture: https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html
- NumPy: https://numpy.org/doc/stable/

## Struktur Folder

```text
01-color-detection/
└── README.md
```

## Tugas Harian

### Hari 1

- Materi: BGR/RGB/HSV dan sampling warna.
- Tugas coding: tampilkan frame dan mask satu warna.
- Target hasil: mask putih pada objek target dan hitam pada area lain.
- Checklist: [ ] HSV [ ] inRange [ ] Mask

### Hari 2

- Materi: contour dan bounding box.
- Tugas coding: ambil contour terbesar dan gambar rectangle.
- Target hasil: objek warna target memiliki kotak.
- Checklist: [ ] Contour [ ] Area [ ] Rectangle

### Hari 3

- Materi: webcam dan stabilitas threshold.
- Tugas coding: tambahkan beberapa warna dan tombol keluar.
- Target hasil: deteksi real-time tidak crash saat objek hilang.
- Checklist: [ ] Webcam [ ] Fallback [ ] `q`

## Checklist Project

- [ ] Menentukan rentang HSV dengan benar.
- [ ] Membuat mask.
- [ ] Mengurangi noise bila diperlukan.
- [ ] Mendeteksi contour.
- [ ] Menggambar bounding box.
- [ ] Menguji kondisi tanpa objek.
- [ ] Menutup webcam dengan aman.

## Cara Menjalankan

Belum ada script pada folder ini. Setelah implementasi dibuat:

```powershell
python projects\01-color-detection\color_detection.py
```

## Expected Output

Jendela webcam menampilkan objek dengan warna target dan bounding box; mask dapat
ditampilkan sebagai jendela kedua.

## Troubleshooting

- Warna tidak terdeteksi: sesuaikan batas HSV terhadap pencahayaan.
- Banyak noise: gunakan blur atau morphology.
- Bounding box bergetar: gunakan contour minimum area.
- Kamera gagal: cek izin kamera dan index device.

## Catatan Keamanan dan Privasi

Webcam dapat menangkap orang dan ruangan. Minta persetujuan dan jangan menyimpan frame
tanpa kebutuhan.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca: