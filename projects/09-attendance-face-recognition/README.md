# Project 09 — Attendance Face Recognition

## Tujuan

Mempelajari alur registered faces, face encoding, matching, timestamp, penyimpanan CSV
atau SQLite, serta pencegahan absensi ganda secara bertanggung jawab.

## Level

Intermediate

## Estimasi Waktu

5–7 hari

## Materi yang Dipelajari

- Face encoding dan distance/threshold matching.
- Unknown faces, registered faces, timestamp, dan cooldown.
- CSV/SQLite dan pencegahan duplicate attendance.

## Library yang Digunakan

- OpenCV: capture dan preprocessing.
- `face-recognition` (optional): encoding/matching; dapat sulit di Windows/Python 3.12.
- MediaPipe atau Haar Cascade: alternatif deteksi wajah.
- `csv`/`sqlite3`/`datetime`: penyimpanan (bawaan Python).

## Instalasi

```powershell
python -m pip install -r ..\..\requirements.txt
```

`face-recognition` sengaja tidak ada di manifest utama. Dependency ini bergantung pada
`dlib` yang dapat memerlukan Visual C++ Build Tools dan wheel yang sesuai. Alternatif
belajar: OpenCV Haar Cascade untuk detection, atau MediaPipe untuk tracking; untuk
recognition gunakan library yang telah diuji di environment terpisah.

## Dokumentasi Resmi

- face-recognition: https://face-recognition.readthedocs.io/
- OpenCV Cascade: https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html
- MediaPipe Face: https://ai.google.dev/edge/mediapipe/solutions/vision/face_detector
- csv: https://docs.python.org/3/library/csv.html
- sqlite3: https://docs.python.org/3/library/sqlite3.html
- datetime: https://docs.python.org/3/library/datetime.html

## Struktur Folder

```text
09-attendance-face-recognition/
└── README.md
```

## Tugas Harian

### Hari 1–2

- Materi: registrasi dan encoding.
- Tugas coding: buat dataset kecil berizin dan encoding.
- Target hasil: wajah terdaftar memiliki identifier internal.
- Checklist: [ ] Consent [ ] Register [ ] Encoding

### Hari 3–4

- Materi: matching dan unknown.
- Tugas coding: uji threshold pada wajah dikenal/tidak dikenal.
- Target hasil: status known/unknown dapat dijelaskan.
- Checklist: [ ] Match [ ] Threshold [ ] Unknown

### Hari 5–6

- Materi: timestamp dan duplicate prevention.
- Tugas coding: simpan satu absensi per orang per hari/sesi.
- Target hasil: CSV/SQLite konsisten dan dapat dicari.
- Checklist: [ ] Timestamp [ ] Unique key [ ] Storage

### Hari 7

- Materi: evaluasi dan threat model.
- Tugas coding: uji false accept/false reject.
- Target hasil: keterbatasan sistem terdokumentasi.
- Checklist: [ ] Evaluation [ ] Review [ ] Retention

## Checklist Project

- [ ] Meminta persetujuan sebelum registrasi.
- [ ] Menyimpan identifier seperlunya.
- [ ] Menangani unknown faces.
- [ ] Menentukan threshold lewat data uji.
- [ ] Mencegah absensi ganda.
- [ ] Melindungi CSV/SQLite.
- [ ] Menyediakan penghapusan data.

## Cara Menjalankan

```powershell
python projects\09-attendance-face-recognition\attendance.py
```

## Expected Output

Frame menampilkan status internal dan log absensi dengan timestamp; satu orang tidak
dicatat berulang sesuai aturan sesi.

## Troubleshooting

- `dlib` gagal build: gunakan alternatif atau environment Python yang kompatibel.
- False match: naikkan threshold kualitas/data dan uji ulang.
- Duplicate: gunakan unique key (identitas + tanggal/sesi).
- Data rusak: gunakan transaksi SQLite dan backup terenkripsi.

## Catatan Keamanan dan Privasi

Face recognition dan attendance memproses data biometrik. Wajib ada persetujuan, tujuan
yang jelas, kontrol akses, retensi terbatas, dan opsi penghapusan. Jangan dipakai sebagai
satu-satunya dasar keputusan penting.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:
