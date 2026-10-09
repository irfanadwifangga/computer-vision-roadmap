# Day 01 — Setup Environment

## Tujuan

Menyiapkan virtual environment dan memastikan Python, OpenCV, NumPy, serta Matplotlib
dapat di-import. Hasil akhirnya adalah environment yang siap dipakai untuk latihan.

## Level

Beginner

## Estimasi Waktu

1 hari

## Materi yang Dipelajari

- `sys.version` dan informasi runtime.
- `venv` untuk environment terisolasi.
- `pip` untuk memasang package.
- Import dan versi OpenCV, NumPy, Matplotlib.
- Perbedaan nama package pip dan nama module Python.

## Library yang Digunakan

- `sys`: membaca informasi Python.
- `cv2` dari `opencv-python`: computer vision.
- `numpy`: operasi array.
- `matplotlib`: visualisasi.

## Instalasi

Dari root repository:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r ..\requirements.txt
```

## Dokumentasi Resmi

- sys: https://docs.python.org/3/library/sys.html
- venv: https://docs.python.org/3/library/venv.html
- pip: https://pip.pypa.io/en/stable/
- OpenCV Python: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- NumPy: https://numpy.org/doc/stable/
- Matplotlib: https://matplotlib.org/stable/

## Struktur Folder

```text
day-01-setup/
├── README.md
└── check_enviroment.py
```

## Tugas Harian

### Hari 1

- Materi: `venv`, `pip`, import module, dan versi package.
- Tugas coding: jalankan `check_enviroment.py`.
- Target hasil: empat versi tampil tanpa `ModuleNotFoundError`.
- Checklist: [ ] Environment aktif [ ] Package terdeteksi [ ] Versi dicatat

## Checklist Project

- [ ] Membuat `.venv`.
- [ ] Mengaktifkan `.venv`.
- [ ] Memasang `requirements.txt`.
- [ ] Menjalankan `check_enviroment.py`.
- [ ] Mencatat versi Python dan package.

## Cara Menjalankan

```powershell
python day-01-setup\check_enviroment.py
```

## Expected Output

Terminal menampilkan `Python version`, `OpenCV version`, `NumPy version`,
`Matplotlib version`, dan `Environment siap digunakan!`.

## Troubleshooting

- `ModuleNotFoundError`: pastikan `.venv` aktif dan gunakan `python -m pip`.
- `python tidak dikenali`: instal Python dan aktifkan opsi PATH.
- PowerShell menolak script: gunakan `activate.bat` lewat Command Prompt.
- Nama file adalah `check_enviroment.py` (bukan `check_environment.py`); pertahankan nama
  existing saat menjalankan.

## Catatan Keamanan dan Privasi

Belum memakai webcam atau data pengguna. Jangan menyimpan token atau credential di
environment dan jangan commit folder `.venv`.

## Catatan Belajar

Tanggal:
Materi:
Hal yang dipahami:
Error:
Solusi:
Eksperimen:
Dokumentasi yang dibaca:

