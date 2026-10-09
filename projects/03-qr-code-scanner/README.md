# Project 03 — QR Code Scanner

## Tujuan

Membaca data QR dari webcam, menampilkan bounding box, menyimpan riwayat scan, dan
mencegah data yang sama dicatat berulang kali.

## Level

Beginner

## Estimasi Waktu

2–3 hari

## Materi yang Dipelajari

- Deteksi dan decoding QR.
- `cv2.QRCodeDetector` atau `pyzbar`.
- Validasi payload, timestamp, history, dan deduplikasi.

## Library yang Digunakan

- OpenCV: capture, preview, dan QRCodeDetector.
- `pyzbar` (optional): decoder alternatif; Windows dapat memerlukan ZBar DLL.
- `csv` dan `datetime`: riwayat dan timestamp (bawaan Python).

## Instalasi

```powershell
python -m pip install -r ..\..\requirements.txt
```

`pyzbar` hanya diperlukan bila tidak memakai `cv2.QRCodeDetector`.

## Dokumentasi Resmi

- QRCodeDetector: https://docs.opencv.org/4.x/de/dc3/classcv_1_1QRCodeDetector.html
- OpenCV video: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
- pyzbar: https://github.com/NaturalHistoryMuseum/pyzbar
- csv: https://docs.python.org/3/library/csv.html
- datetime: https://docs.python.org/3/library/datetime.html

## Struktur Folder

```text
03-qr-code-scanner/
└── README.md
```

## Tugas Harian

### Hari 1

- Materi: QR detection dan decode.
- Tugas coding: baca satu QR dari gambar/frame.
- Target hasil: payload tampil di terminal.
- Checklist: [ ] Detect [ ] Decode [ ] Invalid QR

### Hari 2

- Materi: bounding box dan webcam.
- Tugas coding: gambar polygon/box pada QR.
- Target hasil: QR terdeteksi real-time.
- Checklist: [ ] Webcam [ ] Box [ ] `q`

### Hari 3

- Materi: riwayat dan deduplikasi.
- Tugas coding: simpan payload + timestamp hanya sekali dalam interval tertentu.
- Target hasil: CSV tidak memiliki scan duplikat berurutan.
- Checklist: [ ] CSV [ ] Timestamp [ ] Deduplikasi

## Checklist Project

- [ ] Memilih QRCodeDetector atau pyzbar.
- [ ] Menangani payload kosong.
- [ ] Menampilkan bounding box.
- [ ] Menyimpan riwayat.
- [ ] Mencegah duplikasi.
- [ ] Menutup kamera dengan aman.

## Cara Menjalankan

```powershell
python projects\03-qr-code-scanner\qr_scanner.py
```

## Expected Output

Data QR tampil di frame/terminal dan entry baru tercatat ke file riwayat.

## Troubleshooting

- QR tidak terbaca: perbesar QR, tambah cahaya, dan jaga fokus.
- `pyzbar` gagal load DLL: gunakan `QRCodeDetector` atau pasang ZBar sesuai dokumentasi.
- History berulang: simpan payload terakhir dan timestamp.

## Catatan Keamanan dan Privasi

QR dapat berisi URL, token, atau data pribadi. Jangan membuka URL otomatis dan jangan
menyimpan payload sensitif tanpa persetujuan.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:
