# Project 10 — Sign Language Recognition

## Tujuan

Mengumpulkan dataset gesture tangan berlabel, mengekstrak fitur landmark, melatih
classifier sederhana, mengevaluasi accuracy/confusion matrix, dan memprediksi gesture
secara real-time.

## Level

Intermediate

## Estimasi Waktu

7–10 hari

## Materi yang Dipelajari

- Hand landmarks dan dataset collection.
- Feature extraction, labeling, dan train-test split.
- Random Forest atau KNN.
- Accuracy, confusion matrix, dan prediksi real-time.

## Library yang Digunakan

- MediaPipe: hand landmarks.
- OpenCV: capture dan preview.
- NumPy: feature vector.
- scikit-learn: split, classifier, metrics, dan confusion matrix.
- `csv`/`pathlib`: dataset lokal (bawaan/standard library).

## Instalasi

```powershell
python -m pip install -r ..\..\requirements.txt
```

## Dokumentasi Resmi

- MediaPipe Hand Landmarker: https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker
- scikit-learn Random Forest: https://scikit-learn.org/stable/modules/ensemble.html
- scikit-learn KNN: https://scikit-learn.org/stable/modules/neighbors.html
- train-test split: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
- confusion matrix: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
- classification report: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html

## Struktur Folder

```text
10-sign-language-recognition/
└── README.md
```

## Tugas Harian

### Hari 1–2

- Materi: definisi label dan collection protocol.
- Tugas coding: kumpulkan landmark beberapa gesture dengan persetujuan.
- Target hasil: dataset seimbang dan terdokumentasi.
- Checklist: [ ] Label [ ] Consent [ ] Balance

### Hari 3–4

- Materi: feature extraction dan normalization.
- Tugas coding: ubah landmark menjadi vector relatif terhadap wrist.
- Target hasil: CSV fitur konsisten.
- Checklist: [ ] Feature [ ] Normalize [ ] Missing hand

### Hari 5–6

- Materi: split dan classifier.
- Tugas coding: latih Random Forest/KNN.
- Target hasil: metrik validasi tercatat.
- Checklist: [ ] Split [ ] Train [ ] Accuracy

### Hari 7–10

- Materi: confusion matrix dan real-time inference.
- Tugas coding: tampilkan prediksi serta confidence/status.
- Target hasil: gesture dapat diprediksi pada kondisi baru.
- Checklist: [ ] Matrix [ ] Realtime [ ] Error analysis

## Checklist Project

- [ ] Dataset dikumpulkan dengan izin.
- [ ] Label dan feature vector tervalidasi.
- [ ] Train-test split tidak bocor.
- [ ] Classifier dilatih dan disimpan secara lokal.
- [ ] Accuracy/confusion matrix dianalisis.
- [ ] Gesture tidak dikenal ditangani.
- [ ] Real-time prediction diuji.

## Cara Menjalankan

```powershell
python projects\10-sign-language-recognition\collect_data.py
python projects\10-sign-language-recognition\train_model.py
python projects\10-sign-language-recognition\predict_realtime.py
```

Script tersebut adalah rencana implementasi dan belum tersedia pada fase dokumentasi.

## Expected Output

Dataset berlabel, laporan accuracy/confusion matrix, dan jendela webcam yang menampilkan
prediksi gesture real-time.

## Troubleshooting

- Accuracy tinggi tetapi real-time buruk: cek data leakage dan variasi pencahayaan.
- Landmark hilang: skip frame atau beri label `unknown`.
- Class tidak seimbang: tambah data minoritas dan periksa confusion matrix.
- Prediksi berubah-ubah: gunakan smoothing temporal.

## Catatan Keamanan dan Privasi

Dataset tangan dapat tetap mengandung wajah, suara, atau identitas peserta. Minta
persetujuan penggunaan dataset, simpan metadata minimal, dan jangan mengunggah data
mentah peserta tanpa izin.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:
