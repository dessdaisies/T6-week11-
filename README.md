# T6 Week 11 - Post Manager

## Deskripsi
Aplikasi ini dibuat menggunakan Python dan PySide6 untuk mengelola data post dari REST API. Program ini menampilkan data dalam bentuk tabel dan menyediakan fitur CRUD (Create, Read, Update, Delete).

## Fitur
- Menampilkan daftar post (GET)
- Menampilkan detail post beserta komentar
- Menambah data post (POST)
- Mengedit data post (PUT)
- Menghapus data post (DELETE)
- Menggunakan threading agar UI tidak freeze
- Menampilkan status loading dan selesai

## Teknologi
- Python
- PySide6 (GUI)
- Requests (HTTP Client)

## Struktur Project

- post_manager.py → file utama aplikasi
- README.md → dokumentasi
- screenshots/ → berisi gambar hasil aplikasi

## Screenshot

### Load Data
![Load Data](screenshots/Load-Data.jpeg)

### Tambah Data
![Tambah Data](screenshots/Form-tambah-data.jpeg)

### Detail Post
![Detail Post](screenshots/Detail-post.jpeg)

### Detail Post dengan Komentar
![Detail Komentar](screenshots/Detail-post-dengan-komentar.jpeg)

### Edit Data
![Edit Data](screenshots/Edit-data.jpeg)

### Hapus Data
![Hapus Data](screenshots/Hapus-data.jpeg)

### State Loading
![Loading](screenshots/State-loading.jpeg)

### State Selesai
![Selesai](screenshots/State-selesai.jpeg)

## Cara Menjalankan
1. Aktifkan virtual environment: venv\Scripts\activate
2. Install dependencies: pip install requests PySide6
3. Jalankan program: python post_manager.py

## Author
- Nama: Deswita Salsabila
- NIM: F1D02410004
- Kelas: C
