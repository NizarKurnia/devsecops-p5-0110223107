# Aplikasi Kalkulator API (DevSecOps P5)

**1. Nama Aplikasi & Fungsinya**
Aplikasi ini bernama "Kalkulator API". Fungsinya adalah menyediakan endpoint REST API sederhana untuk melakukan operasi matematika dasar (penjumlahan dan pengurangan).

**2. Bahasa/Framework yang Digunakan**
- **Bahasa:** Python 3
- **Framework:** Flask
- **Testing:** Pytest
- **SAST Tool:** Bandit

**3. Cara Menjalankan Aplikasi**
Pastikan Python sudah terinstal, lalu jalankan perintah berikut di terminal:
`pip install -r requirements.txt`
`python app.py`
Aplikasi akan berjalan di `http://127.0.0.1:5000`.

**4. Overview Pipeline CI/CD**
Pipeline diimplementasikan menggunakan GitHub Actions (`devsecops.yml`). Terdapat dua job utama yang berjalan pada runner `ubuntu-latest`:
- **Job Build**: Melakukan instalasi dependensi Python dan menjalankan *unit test* menggunakan Pytest untuk memastikan kode bebas error secara fungsional.
- **Job SAST-Scan**: Berjalan setelah job *build* berhasil (menggunakan *needs*). Job ini menjalankan tool **Bandit** untuk memindai kerentanan keamanan pada source code Python.