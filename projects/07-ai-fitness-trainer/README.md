# Project 07 — AI Fitness Trainer

## Tujuan

Membuat penghitung squat, push-up, atau bicep curl berbasis MediaPipe Pose dengan
perhitungan sudut, state machine, dan feedback postur.

## Level

Intermediate

## Estimasi Waktu

5–7 hari

## Materi yang Dipelajari

- Pose landmarks dan koordinat.
- Sudut tiga titik.
- State machine gerakan, counter, feedback, dan pengurangan false counting.

## Library yang Digunakan

- MediaPipe Pose: landmark tubuh.
- OpenCV: webcam, overlay, dan UI.
- NumPy/math: koordinat dan sudut.

## Instalasi

```powershell
python -m pip install -r ..\..\requirements.txt
```

## Dokumentasi Resmi

- MediaPipe Pose Landmarker: https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker
- OpenCV drawing: https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html
- NumPy: https://numpy.org/doc/stable/

## Struktur Folder

```text
07-ai-fitness-trainer/
└── README.md
```

## Tugas Harian

### Hari 1

- Materi: pose landmarks.
- Tugas coding: gambar skeleton.
- Target hasil: titik tubuh terlihat konsisten.
- Checklist: [ ] Pose [ ] Landmark [ ] Overlay

### Hari 2

- Materi: sudut bahu/pinggul/lutut atau siku.
- Tugas coding: hitung dan tampilkan sudut.
- Target hasil: sudut berubah sesuai gerakan.
- Checklist: [ ] Angle [ ] Visibility [ ] Threshold

### Hari 3

- Materi: state machine.
- Tugas coding: state turun/naik untuk squat atau curl.
- Target hasil: satu repetisi dihitung sekali.
- Checklist: [ ] State [ ] Counter [ ] Reset

### Hari 4–5

- Materi: feedback postur dan false count.
- Tugas coding: tambahkan cooldown, visibility check, dan instruksi.
- Target hasil: counter stabil pada beberapa kecepatan gerak.
- Checklist: [ ] Feedback [ ] Cooldown [ ] Test

## Checklist Project

- [ ] Pose landmarks tampil.
- [ ] Sudut dihitung dengan benar.
- [ ] State machine terdokumentasi.
- [ ] Counter hanya naik pada transisi valid.
- [ ] Feedback postur jelas.
- [ ] Kondisi landmark hilang ditangani.

## Cara Menjalankan

```powershell
python projects\07-ai-fitness-trainer\fitness_trainer.py
```

## Expected Output

Skeleton, sudut, state, counter, dan feedback tampil di video real-time.

## Troubleshooting

- Counter ganda: tambahkan state transition dan cooldown.
- Pose tidak stabil: letakkan kamera lebih jauh dan gunakan cahaya cukup.
- Sudut salah: cek urutan tiga titik dan koordinat image.
- False feedback: cek visibility dan kalibrasi threshold.

## Catatan Keamanan dan Privasi

Ini bukan alat medis. Jangan menyimpan video latihan tanpa persetujuan dan sampaikan
bahwa feedback hanya untuk pembelajaran.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:
