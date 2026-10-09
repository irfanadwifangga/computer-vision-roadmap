# Project 02 — Face Detection

## Tujuan

Mendeteksi wajah pada gambar atau webcam menggunakan Haar Cascade, menggambar bounding
box, menghitung jumlah wajah, dan menyimpan screenshot bila diperlukan.

## Level

Beginner

## Estimasi Waktu

2–3 hari

## Materi yang Dipelajari

- Haar Cascade dan `CascadeClassifier`.
- Grayscale, `detectMultiScale()`, bounding box, counter, dan screenshot.

## Library yang Digunakan

- OpenCV: cascade, webcam, grayscale, rectangle, dan image write.
- `pathlib`: path screenshot.

## Instalasi

```powershell
python -m pip install -r ..\..\requirements.txt
```

## Dokumentasi Resmi

- Cascade Classifier: https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html
- CascadeClassifier: https://docs.opencv.org/4.x/d1/de5/classcv_1_1CascadeClassifier.html
- Video I/O: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
- imwrite: https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html

## Struktur Folder

```text
02-face-detection/
└── README.md
```

## Tugas Harian

### Hari 1

- Materi: cascade dan grayscale.
- Tugas coding: deteksi wajah dari satu gambar.
- Target hasil: wajah diberi kotak.
- Checklist: [ ] Load cascade [ ] Grayscale [ ] Detect

### Hari 2

- Materi: webcam dan jumlah wajah.
- Tugas coding: tampilkan counter wajah real-time.
- Target hasil: jumlah wajah terlihat di frame.
- Checklist: [ ] Webcam [ ] Counter [ ] Empty frame

### Hari 3

- Materi: screenshot dan false positive.
- Tugas coding: simpan frame dengan tombol tertentu.
- Target hasil: screenshot tersimpan dengan izin.
- Checklist: [ ] Screenshot [ ] Path [ ] Uji cahaya

## Checklist Project

- [ ] Menemukan file cascade.
- [ ] Mengubah frame ke grayscale.
- [ ] Menjalankan `detectMultiScale()`.
- [ ] Menggambar bounding box.
- [ ] Menghitung wajah.
- [ ] Menyimpan screenshot dengan persetujuan.

## Cara Menjalankan

```powershell
python projects\02-face-detection\face_detection.py
```

Nama script adalah rencana implementasi dan belum tersedia saat dokumentasi dibuat.

## Expected Output

Wajah yang terdeteksi diberi kotak dan teks jumlah wajah; screenshot tersimpan jika
tombol capture ditekan.

## Troubleshooting

- Cascade tidak ditemukan: gunakan path dari `cv2.data.haarcascades`.
- Wajah luput: tambah ukuran gambar atau perbaiki pencahayaan.
- False positive: naikkan `minNeighbors`.
- FPS rendah: kecilkan resolusi frame.

## Catatan Keamanan dan Privasi

Wajah adalah data biometrik. Minta persetujuan eksplisit, minimalkan penyimpanan, dan
jangan membagikan screenshot identitas tanpa izin.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:
