# Day 02 — Image Basics

## Tujuan

Memahami gambar sebagai NumPy array dan melakukan operasi baca, tulis, resize, crop,
konversi warna, rotasi, flip, serta blur. Hasil akhirnya adalah beberapa file gambar di
folder `output/` dan tampilan perbandingan dengan Matplotlib.

## Level

Beginner

## Estimasi Waktu

2 hari

## Materi yang Dipelajari

- `cv2.imread()`, `imwrite()`, `resize()`, `cvtColor()`, `rotate()`, `flip()`,
  `GaussianBlur()`.
- BGR, RGB, dan grayscale.
- `shape`, slicing NumPy, dan koordinat gambar.
- `matplotlib.pyplot.imshow()`.

## Library yang Digunakan

- OpenCV: transformasi dan penyimpanan gambar.
- NumPy: array dan crop melalui slicing.
- Matplotlib: menampilkan hasil dengan `imshow()`.
- `pathlib`: membentuk path portabel.

## Instalasi

```powershell
python -m pip install -r ..\requirements.txt
```

## Dokumentasi Resmi

- `imread`: https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html
- `imwrite`: https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html
- Geometric transforms: https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html
- Color conversions: https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html
- Smoothing: https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
- NumPy indexing: https://numpy.org/doc/stable/user/basics.indexing.html
- `imshow`: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html
- pathlib: https://docs.python.org/3/library/pathlib.html

## Struktur Folder

```text
day-02-image-basics/
├── README.md
├── image_basics.py
├── assets/
│   └── sample.jpg
└── output/
    ├── copy.jpg
    ├── cropped.jpg
    ├── gray.jpg
    └── resized.jpg
```

## Tugas Harian

### Hari 1

- Materi: baca/tulis, shape, BGR/RGB/grayscale, resize dan crop.
- Tugas coding: jalankan script dan ubah ukuran resize.
- Target hasil: `copy.jpg`, `resized.jpg`, `cropped.jpg`, `gray.jpg`.
- Checklist: [ ] Baca [ ] Tulis [ ] Resize [ ] Crop

### Hari 2

- Materi: rotate, flip, Gaussian blur, dan visualisasi.
- Tugas coding: tambahkan hasil rotate/flip/blur dengan nama file terpisah.
- Target hasil: dapat menjelaskan perbedaan warna dan efek setiap transformasi.
- Checklist: [ ] Rotate [ ] Flip [ ] Blur [ ] Bandingkan hasil

## Checklist Project

- [ ] Memahami array `image_bgr`.
- [ ] Menguji `imread()` dan `imwrite()`.
- [ ] Menguji resize dan slicing crop.
- [ ] Mengubah BGR ke RGB.
- [ ] Membuat grayscale.
- [ ] Mencoba rotate, flip, dan Gaussian blur.
- [ ] Memeriksa file hasil di `output/`.

## Cara Menjalankan

```powershell
python day-02-image-basics\image_basics.py
```

## Expected Output

Terminal menampilkan nama file, ukuran, jumlah channel, dan lokasi output. Jendela
Matplotlib menampilkan Original, Resized, Cropped, dan Grayscale.

## Troubleshooting

- Gambar `None`: periksa `assets/sample.jpg` dan path relatif.
- Warna tampak biru/merah tertukar: OpenCV memakai BGR, Matplotlib umumnya RGB.
- Jendela tidak muncul: jalankan dari desktop session dan cek backend Matplotlib.
- Output lama membingungkan: gunakan nama file baru atau hapus hanya output hasil eksperimen.

## Catatan Keamanan dan Privasi

Gunakan gambar milik sendiri atau yang lisensinya jelas. Jangan memasukkan foto pribadi
ke repository publik.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:

