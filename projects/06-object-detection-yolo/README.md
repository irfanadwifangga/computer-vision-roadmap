# Project 06 — Object Detection dengan YOLO

## Tujuan

Menggunakan model pretrained Ultralytics YOLO untuk mendeteksi objek dari gambar, video,
dan webcam, menampilkan label/confidence, menghitung objek, serta menyimpan hasil.

## Level

Intermediate

## Estimasi Waktu

4–5 hari

## Materi yang Dipelajari

- Model pretrained dan inference.
- Bounding box, class label, confidence score.
- Gambar/video/webcam, object counting, dan export hasil.

## Library yang Digunakan

- Ultralytics: load model, predict, plot, dan tracking/counting.
- OpenCV: input/output video bila diperlukan.
- NumPy: array frame.

## Instalasi

```powershell
python -m pip install -r ..\..\requirements.txt
```

Ultralytics ada di requirements optional karena dapat mengunduh model dan dependensi
tambahan saat pertama dipakai.

## Dokumentasi Resmi

- Ultralytics Predict: https://docs.ultralytics.com/modes/predict/
- Ultralytics Track: https://docs.ultralytics.com/modes/track/
- Ultralytics Python usage: https://docs.ultralytics.com/usage/python/
- OpenCV video: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

## Struktur Folder

```text
06-object-detection-yolo/
└── README.md
```

## Tugas Harian

### Hari 1

- Materi: model pretrained dan inference gambar.
- Tugas coding: deteksi satu gambar.
- Target hasil: label dan box terlihat.
- Checklist: [ ] Model [ ] Image [ ] Plot

### Hari 2

- Materi: confidence dan class filter.
- Tugas coding: ubah threshold dan pilih kelas.
- Target hasil: hanya deteksi relevan yang ditampilkan.
- Checklist: [ ] Confidence [ ] Class [ ] Filter

### Hari 3

- Materi: video/webcam.
- Tugas coding: inference frame demi frame.
- Target hasil: deteksi real-time dapat dihentikan.
- Checklist: [ ] Video [ ] Webcam [ ] FPS

### Hari 4

- Materi: counting dan penyimpanan.
- Tugas coding: hitung objek unik dan simpan annotated output.
- Target hasil: output dapat diputar dan jumlah objek masuk akal.
- Checklist: [ ] Count [ ] Save [ ] Evaluate

## Checklist Project

- [ ] Memilih model dan memahami lisensinya.
- [ ] Mencoba gambar, video, dan webcam.
- [ ] Menampilkan label/confidence.
- [ ] Menyaring confidence.
- [ ] Menghitung objek.
- [ ] Menyimpan hasil tanpa commit model besar.

## Cara Menjalankan

```powershell
python projects\06-object-detection-yolo\yolo_detection.py
```

## Expected Output

Frame berisi bounding box, label kelas, dan confidence; output annotated tersimpan jika
mode save diaktifkan.

## Troubleshooting

- Model tidak ditemukan: biarkan download resmi atau sediakan path model lokal.
- CUDA tidak tersedia: gunakan CPU dan turunkan resolusi.
- Deteksi lemah: periksa confidence, ukuran objek, dan pencahayaan.
- Output terlalu besar: batasi resolusi dan jangan commit file model/video.

## Catatan Keamanan dan Privasi

Video bisa memuat orang, lokasi, atau kendaraan. Pastikan hak penggunaan data dan samarkan
identitas sebelum membagikan output.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:
