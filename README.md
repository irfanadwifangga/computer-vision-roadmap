# Computer Vision Roadmap dengan Python

Roadmap belajar Computer Vision bertahap dari dasar image processing hingga project intermediate seperti YOLO, OCR, pose estimation, dan pengenalan gesture.

## Deskripsi Project

Repository ini berisi materi harian, contoh kode yang sudah tersedia, dan spesifikasi project latihan. Fokus saat ini adalah dokumentasi belajar; implementasi project lanjutan dibuat bertahap setelah materi dasarnya dipahami.

## Level

Beginner hingga Intermediate.

## Estimasi Waktu

Sekitar 4–8 minggu dengan kecepatan 1–2 jam per hari.

## Materi yang Dipelajari

Python environment, NumPy array, OpenCV image/video processing, webcam, detection, tracking, OCR, pose estimation, dan machine learning dasar.

## Library yang Digunakan

OpenCV, NumPy, Matplotlib, serta dependency optional MediaPipe, Ultralytics, OCR, pycaw, pandas, dan scikit-learn.

## Instalasi

Gunakan [requirements.txt](requirements.txt) untuk dependency utama. Dependency optional dipasang per project dari [requirements-optional.txt](requirements-optional.txt).

## Tujuan Roadmap

- Memahami array gambar dan operasi dasar OpenCV.
- Membuat aplikasi webcam real-time.
- Memahami detection, tracking, OCR, pose, dan machine learning dasar.
- Membangun kebiasaan mencatat eksperimen, error, dan dokumentasi resmi yang dibaca.

## Prasyarat

- Windows 10/11.
- Python 3.10+; Python 3.12 dapat digunakan untuk dependency utama.
- PowerShell atau terminal Windows.
- Webcam untuk materi video dan project real-time.
- Git untuk menyimpan progress.

## Setup Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Jika PowerShell memblokir script, gunakan Command Prompt:

```bat
.venv\Scripts\activate.bat
```

Dependency khusus project ada di [requirements-optional.txt](requirements-optional.txt). Instal hanya dependency yang diperlukan dan jangan menjalankan instalasi otomatis tanpa memeriksa kompatibilitasnya.

## Struktur Folder

```text
computer-vision-roadmap/
├── README.md
├── .gitignore
├── requirements.txt
├── requirements-optional.txt
├── day-01-setup/
│   ├── README.md
│   └── check_enviroment.py
├── day-02-image-basics/
│   ├── README.md
│   ├── image_basics.py
│   ├── assets/
│   └── output/
├── day-03-webcam-basics/
│   └── README.md
└── projects/
    ├── 01-color-detection/README.md
    ├── 02-face-detection/README.md
    ├── 03-qr-code-scanner/README.md
    ├── 04-virtual-drawing-board/README.md
    ├── 05-hand-gesture-volume-controller/README.md
    ├── 06-object-detection-yolo/README.md
    ├── 07-ai-fitness-trainer/README.md
    ├── 08-license-plate-recognition/README.md
    ├── 09-attendance-face-recognition/README.md
    └── 10-sign-language-recognition/README.md
```

Folder `.venv/`, output, model, video, dan dataset lokal tidak diunggah ke Git.

## Urutan Roadmap

1. [Day 1 — Setup](day-01-setup/README.md)
2. [Day 2 — Image Basics](day-02-image-basics/README.md)
3. [Day 3 — Webcam Basics](day-03-webcam-basics/README.md)
4. Project warna dan wajah
5. QR scanner dan virtual drawing board
6. Hand gesture, YOLO, dan fitness trainer
7. OCR plat nomor, attendance, dan sign language recognition

## Tugas Harian

Ikuti tugas harian pada README setiap folder. Selesaikan satu tahap, jalankan eksperimen, catat error/solusi, lalu lanjut ke tahap berikutnya.

## Checklist Project

- [x] Menyelesaikan setup dan image basics.
- [ ] Menyelesaikan webcam basics.
- [ ] Menyelesaikan project sesuai urutan.
- [ ] Menulis catatan eksperimen untuk setiap tahap.

## Expected Output

Setiap tahap menghasilkan pemahaman konsep, output yang dapat diamati, dan catatan reproduksi. Project yang belum memiliki script tidak dianggap selesai hanya karena README sudah tersedia.

## Troubleshooting

- Pastikan terminal berada di root repository.
- Pastikan virtual environment aktif.
- Gunakan path Windows dengan `\` pada PowerShell.
- Baca troubleshooting pada README folder yang sedang dikerjakan.

## Daftar Project

| Project | Level | Fokus |
| --- | --- | --- |
| [01 Color Detection](projects/01-color-detection/README.md) | Beginner | HSV, mask, contour |
| [02 Face Detection](projects/02-face-detection/README.md) | Beginner | Haar Cascade |
| [03 QR Code Scanner](projects/03-qr-code-scanner/README.md) | Beginner | QR dan riwayat scan |
| [04 Virtual Drawing Board](projects/04-virtual-drawing-board/README.md) | Beginner | Hand landmarks dan canvas |
| [05 Volume Controller](projects/05-hand-gesture-volume-controller/README.md) | Intermediate | Gesture dan pycaw |
| [06 Object Detection YOLO](projects/06-object-detection-yolo/README.md) | Intermediate | Bounding box dan confidence |
| [07 AI Fitness Trainer](projects/07-ai-fitness-trainer/README.md) | Intermediate | Pose dan state machine |
| [08 License Plate Recognition](projects/08-license-plate-recognition/README.md) | Intermediate | OCR dan CSV |
| [09 Attendance Face Recognition](projects/09-attendance-face-recognition/README.md) | Intermediate | Encoding dan absensi |
| [10 Sign Language Recognition](projects/10-sign-language-recognition/README.md) | Intermediate | Dataset dan classifier |

## Dokumentasi Resmi

- Python: https://docs.python.org/3/
- `venv`: https://docs.python.org/3/library/venv.html
- `pip`: https://pip.pypa.io/en/stable/
- `sys`: https://docs.python.org/3/library/sys.html
- OpenCV: https://docs.opencv.org/4.x/
- NumPy: https://numpy.org/doc/stable/
- Matplotlib: https://matplotlib.org/stable/
- MediaPipe: https://ai.google.dev/edge/mediapipe/solutions/guide
- Ultralytics: https://docs.ultralytics.com/
- scikit-learn: https://scikit-learn.org/stable/
- EasyOCR: https://www.jaided.ai/easyocr/
- pyzbar: https://github.com/NaturalHistoryMuseum/pyzbar
- pycaw: https://github.com/AndreMiras/pycaw

## Checklist Progress

- [ ] Day 1 selesai dan environment terverifikasi.
- [ ] Day 2 selesai dan output gambar dipahami.
- [ ] Day 3 selesai dan webcam dapat dibuka/ditutup dengan aman.
- [ ] Project 1–3 selesai.
- [ ] Project 4–7 selesai.
- [ ] Project 8–10 selesai dengan catatan privasi.
- [ ] Setiap eksperimen dicatat di bagian Catatan Belajar.

## Catatan Penggunaan Webcam

Pastikan kamera tidak sedang dipakai aplikasi lain. Gunakan `q` atau tombol yang dijelaskan oleh program untuk berhenti, lalu selalu panggil `release()` dan `destroyAllWindows()`. Jangan merekam orang tanpa pemberitahuan.

## Catatan Privasi

Wajah, plat nomor, rekaman webcam, dan data kehadiran adalah data sensitif. Gunakan data dengan persetujuan, simpan lokal secara aman, samarkan hasil saat dibagikan, dan jangan mengunggah dataset atau rekaman pengguna ke repository publik.

## Cara Menjalankan Project

Aktifkan environment, lalu jalankan script dari root repository:

```powershell
.\.venv\Scripts\Activate.ps1
python day-01-setup\check_enviroment.py
python day-02-image-basics\image_basics.py
```

Project yang belum memiliki script hanya memiliki roadmap dokumentasi; script dibuat pada fase belajar berikutnya.

## Cara Melakukan Commit Git

```powershell
git status
git add README.md requirements.txt requirements-optional.txt day-01-setup day-02-image-basics day-03-webcam-basics projects
git commit -m "docs: lengkapi computer vision roadmap"
git log --oneline -5
```

Periksa `git diff --cached` sebelum commit dan jangan pernah menambahkan `.venv`, credential, rekaman, dataset pribadi, atau model besar.

## Catatan Belajar

Tanggal: Materi: Hal yang dipahami: Error: Solusi: Eksperimen: Dokumentasi yang dibaca:
