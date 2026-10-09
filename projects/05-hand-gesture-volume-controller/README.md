# Project 05 — Hand Gesture Volume Controller

## Tujuan

Mengontrol volume Windows berdasarkan jarak ibu jari dan telunjuk, menampilkan volume
bar, dan tetap aman saat tangan tidak terdeteksi.

## Level

Intermediate

## Estimasi Waktu

3–4 hari

## Materi yang Dipelajari

- Hand tracking dan landmark.
- Jarak Euclidean ibu jari–telunjuk.
- Mapping jarak ke rentang volume.
- pycaw, volume bar, fallback, dan smoothing.

## Library yang Digunakan

- MediaPipe: hand landmarks.
- OpenCV: webcam dan UI.
- `math`: perhitungan jarak (bawaan Python).
- pycaw/comtypes: endpoint audio Windows.

## Instalasi

```powershell
python -m pip install -r ..\..\requirements.txt
```

Instal `pycaw` dan `comtypes` dari [requirements-optional.txt](../../requirements-optional.txt)
hanya di Windows.

## Dokumentasi Resmi

- MediaPipe Hands: https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker
- pycaw: https://github.com/AndreMiras/pycaw
- comtypes: https://comtypes.readthedocs.io/
- OpenCV VideoCapture: https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html

## Struktur Folder

```text
05-hand-gesture-volume-controller/
└── README.md
```

## Tugas Harian

### Hari 1

- Materi: dua landmark dan jarak.
- Tugas coding: tampilkan jarak di frame.
- Target hasil: jarak berubah sesuai gesture.
- Checklist: [ ] Landmark [ ] Distance [ ] Label

### Hari 2

- Materi: mapping dan volume bar.
- Tugas coding: mapping jarak ke 0–100%.
- Target hasil: bar bergerak halus.
- Checklist: [ ] Mapping [ ] Clamp [ ] Bar

### Hari 3

- Materi: pycaw dan fallback.
- Tugas coding: ubah endpoint volume, tangani tangan hilang.
- Target hasil: volume tidak meloncat dan tidak error.
- Checklist: [ ] pycaw [ ] Fallback [ ] Smoothing

## Checklist Project

- [ ] Menghitung jarak landmark.
- [ ] Membatasi nilai mapping.
- [ ] Menghubungkan pycaw.
- [ ] Menampilkan volume bar.
- [ ] Menangani tangan tidak terdeteksi.
- [ ] Menguji hanya pada Windows.

## Cara Menjalankan

```powershell
python projects\05-hand-gesture-volume-controller\volume_controller.py
```

## Expected Output

Jarak gesture dan volume bar tampil; mendekatkan jari menurunkan/menaikkan volume sesuai
mapping yang dipilih.

## Troubleshooting

- pycaw import gagal: pastikan Windows dan dependency optional terpasang.
- Tidak ada endpoint: cek perangkat audio default Windows.
- Volume bergetar: gunakan smoothing dan dead zone.
- Tangan hilang: pertahankan volume terakhir dan tampilkan status.

## Catatan Keamanan dan Privasi

Webcam tetap aktif dan aplikasi mengubah audio sistem. Tampilkan indikator kamera dan
jangan merekam frame.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:
