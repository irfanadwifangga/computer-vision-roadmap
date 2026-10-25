# Day 03 — Webcam dan Video Basics

## Tujuan

Memahami loop frame real-time menggunakan webcam, menghitung FPS, dan menyimpan video dengan `VideoWriter`. Hasil akhirnya adalah rancangan aplikasi webcam yang berhenti dengan aman.

## Level

Beginner

## Estimasi Waktu

2 hari

## Materi yang Dipelajari

- `cv2.VideoCapture()`, `read()`, dan `isOpened()`.
- `cv2.imshow()` dan `cv2.waitKey()`.
- `release()` serta `destroyAllWindows()`.
- FPS, codec, resolusi, dan `cv2.VideoWriter()`.

## Library yang Digunakan

- OpenCV: capture, preview, keyboard input, dan penyimpanan video.
- `time`: pengukuran interval/FPS bila diperlukan (bawaan Python).

## Instalasi

```powershell
python -m pip install -r ..\requirements.txt
```

## Dokumentasi Resmi

- Video I/O: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
- `VideoCapture`: https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html
- `imshow`: https://docs.opencv.org/4.x/d7/dfc/group__highgui.html
- `waitKey`: https://docs.opencv.org/4.x/d7/dfc/group__highgui.html
- `VideoWriter`: https://docs.opencv.org/4.x/dd/d9e/classcv_1_1VideoWriter.html

## Struktur Folder

```text
day-03-webcam-basics/****
└── README.md
```

## Tugas Harian

### Hari 1

- Materi: membuka kamera, membaca frame, dan keluar dengan tombol `q`.
- Tugas coding: buat script latihan lokal tanpa menyimpan video dahulu.
- Target hasil: preview webcam tampil dan berhenti tanpa crash.
- Checklist: [x] Capture [x] Preview [x] `q` [x] Release

### Hari 2

- Materi: FPS dan VideoWriter.
- Tugas coding: tampilkan FPS dan simpan video ke file lokal.
- Target hasil: video dapat diputar dan resource selalu dilepas.
- Checklist: [ ] FPS [ ] Codec [ ] Writer [ ] Cleanup

## Checklist Project

- [x] Cek `isOpened()`.
- [x] Tangani frame gagal dibaca.
- [x] Tampilkan FPS.
- [x] Gunakan `waitKey()` dengan benar.
- [x] Panggil `release()` dan `destroyAllWindows()`.
- [ ] Uji penyimpanan video.

## Cara Menjalankan

Belum ada script pada folder ini. Setelah script dibuat, jalankan dari root:

```powershell
python day-03-webcam-basics\nama_script.py
```

## Expected Output

Jendela video real-time tampil, FPS terlihat bila diaktifkan, dan tombol `q` menutup jendela serta menghasilkan file video bila recording diaktifkan.

## Troubleshooting

- Kamera gagal dibuka: tutup aplikasi lain atau coba index `1`.
- Video hitam: periksa izin kamera Windows.
- File video rusak: gunakan ukuran frame dan codec yang konsisten.
- Window tidak menutup: pastikan `waitKey()` dipanggil di dalam loop.

## Catatan Keamanan dan Privasi

Webcam dapat merekam wajah dan lingkungan sekitar. Minta persetujuan, hindari merekam layar/data sensitif, dan simpan video di lokasi lokal yang aman.

## Catatan Belajar

Tanggal: Materi: Hal yang dipahami: Error: Solusi: Eksperimen: Dokumentasi yang dibaca:
