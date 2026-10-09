# Project 08 — License Plate Recognition

## Tujuan

Membuat pipeline edukasi untuk preprocessing, menemukan region plat nomor, membaca teks
dengan OCR, membersihkan hasil, dan menyimpan hasil ke CSV.

## Level

Intermediate

## Estimasi Waktu

5–7 hari

## Materi yang Dipelajari

- Grayscale, thresholding, edge detection, contour, dan ROI.
- EasyOCR atau Tesseract.
- Normalisasi hasil OCR dan CSV.

## Library yang Digunakan

- OpenCV: preprocessing dan contour.
- EasyOCR (optional): pembacaan teks.
- `pandas` (optional) atau `csv`: tabel hasil.

## Instalasi

```powershell
python -m pip install -r ..\..\requirements.txt
```

Pilih EasyOCR atau Tesseract sesuai kebutuhan. Jangan memasang keduanya tanpa alasan.

## Dokumentasi Resmi

- Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
- Canny edge: https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
- Contours: https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
- EasyOCR: https://www.jaided.ai/easyocr/
- pandas: https://pandas.pydata.org/docs/
- csv: https://docs.python.org/3/library/csv.html

## Struktur Folder

```text
08-license-plate-recognition/
└── README.md
```

## Tugas Harian

### Hari 1

- Materi: grayscale, blur, threshold, edge.
- Tugas coding: bandingkan setiap preprocessing.
- Target hasil: plat menjadi ROI yang kontras.
- Checklist: [ ] Gray [ ] Threshold [ ] Edge

### Hari 2–3

- Materi: contour dan ROI.
- Tugas coding: pilih kandidat plat berdasarkan bentuk/aspect ratio.
- Target hasil: ROI plat terpotong.
- Checklist: [ ] Contour [ ] ROI [ ] Filter

### Hari 4–5

- Materi: OCR dan cleaning.
- Tugas coding: baca teks dan normalisasi karakter.
- Target hasil: teks OCR dan confidence tercatat.
- Checklist: [ ] OCR [ ] Cleaning [ ] Confidence

### Hari 6–7

- Materi: CSV dan evaluasi.
- Tugas coding: simpan timestamp, path, hasil, dan status review.
- Target hasil: tabel hasil dapat diaudit.
- Checklist: [ ] CSV [ ] Test set [ ] Error analysis

## Checklist Project

- [ ] Pipeline preprocessing jelas.
- [ ] Kandidat ROI difilter.
- [ ] OCR memiliki fallback/error handling.
- [ ] Hasil dibersihkan tanpa mengubah bukti asli.
- [ ] CSV tidak menyimpan data lebih dari kebutuhan.
- [ ] Akurasi diuji pada dataset berizin.

## Cara Menjalankan

```powershell
python projects\08-license-plate-recognition\plate_recognition.py
```

## Expected Output

Gambar menampilkan ROI plat dan hasil OCR; CSV menyimpan hasil beserta timestamp/status.

## Troubleshooting

- OCR salah: perbaiki crop, threshold, skala, dan whitelist karakter.
- Plat tidak ditemukan: longgarkan aspect ratio dan uji pencahayaan.
- EasyOCR lambat: gunakan CPU/resolusi lebih kecil dan cache reader.
- CSV bocor: hapus data uji sebelum berbagi.

## Catatan Keamanan dan Privasi

Plat nomor dapat mengidentifikasi kendaraan/lokasi. Gunakan data dengan dasar hukum dan
persetujuan yang sesuai, minimalkan retensi, dan samarkan saat dipublikasikan.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:
