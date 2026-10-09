# Project 04 — Virtual Drawing Board

## Tujuan

Menggunakan MediaPipe Hand Tracking untuk mengambil posisi ujung jari dan menggambar
di canvas virtual, termasuk pemilihan warna, eraser, dan clear canvas.

## Level

Beginner

## Estimasi Waktu

3–4 hari

## Materi yang Dipelajari

- Hand landmarks dan koordinat normalized.
- Posisi ujung telunjuk dan gesture memilih mode.
- Canvas NumPy, warna, eraser, dan smoothing.

## Library yang Digunakan

- MediaPipe: hand detection/tracking dan landmarks.
- OpenCV: webcam, drawing, UI, dan compositing.
- NumPy: canvas dan operasi array.

## Instalasi

```powershell
python -m pip install -r ..\..\requirements.txt
```

## Dokumentasi Resmi

- MediaPipe Hand Landmarker: https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker
- OpenCV drawing: https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html
- NumPy: https://numpy.org/doc/stable/

## Struktur Folder

```text
04-virtual-drawing-board/
└── README.md
```

## Tugas Harian

### Hari 1

- Materi: landmarks dan koordinat.
- Tugas coding: tampilkan titik tangan.
- Target hasil: ujung telunjuk terlacak.
- Checklist: [ ] Hands [ ] Landmark [ ] Coordinate

### Hari 2

- Materi: canvas dan drawing.
- Tugas coding: gambar garis mengikuti telunjuk.
- Target hasil: garis halus muncul pada canvas.
- Checklist: [ ] Canvas [ ] Line [ ] Smoothing

### Hari 3

- Materi: warna, eraser, clear.
- Tugas coding: tambahkan toolbar gesture/tombol.
- Target hasil: warna, eraser, dan clear berfungsi.
- Checklist: [ ] Warna [ ] Eraser [ ] Clear

## Checklist Project

- [ ] Tracking tangan stabil.
- [ ] Konversi koordinat landmark ke piksel.
- [ ] Canvas terpisah dari frame.
- [ ] Pemilihan warna.
- [ ] Eraser.
- [ ] Clear canvas.
- [ ] Cleanup kamera.

## Cara Menjalankan

```powershell
python projects\04-virtual-drawing-board\virtual_drawing_board.py
```

## Expected Output

Gerakan telunjuk menggambar garis; mode warna dan eraser dapat dipilih; clear
menghapus canvas.

## Troubleshooting

- Tangan tidak terdeteksi: perbaiki cahaya dan posisi tangan.
- Garis melompat: gunakan smoothing/riwayat titik.
- Canvas tertutup frame: gabungkan dengan alpha atau tampilkan side-by-side.
- FPS rendah: turunkan resolusi webcam.

## Catatan Keamanan dan Privasi

Webcam memproses gambar tangan/wajah. Proses lokal, jangan simpan frame tanpa
persetujuan, dan beri tahu pengguna saat kamera aktif.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:
