# Kumpulan Aplikasi Python Bawaan (DevSecOps P5)

**1. Nama Aplikasi & Fungsinya**
Proyek ini berisi kumpulan script aplikasi Python yang dapat berjalan secara masing-masing tanpa library tambahan:
- `web_server.py`: Menjalankan HTTP web server lokal.
- `system_info.py`: Menampilkan informasi sistem operasi.
- `file_manager.py`: Mengotomatisasi pembuatan dan pembacaan file log.
- `math_operations.py`: Menghitung operasi matematika kompleks (faktorial).

**2. Bahasa/Framework yang Digunakan**
- **Bahasa:** Python 3 (Pure Python Standard Library, tanpa eksternal library).
- **Testing:** `unittest` (Bawaan Python).
- **SAST Tool:** Bandit.

**3. Cara Menjalankan Aplikasi**
Karena menggunakan library bawaan Python, tidak perlu instalasi dependencies. Anda dapat langsung menjalankan masing-masing aplikasi di terminal:
- `python web_server.py`
- `python system_info.py`
- `python file_manager.py`
- `python math_operations.py`

**4. Overview Pipeline CI/CD**
Pipeline CI/CD dibuat menggunakan GitHub Actions (`devsecops.yml`).
- **Job Build**: Menjalankan *unit test* menggunakan module `unittest` bawaan Python (`python -m unittest test_apps.py`) untuk memvalidasi fungsi logika.
- **Job SAST-Scan**: Berjalan setelah job build berhasil. Job ini menginstal tool keamanan **Bandit** melalui pip dan memindai semua source code Python untuk mendeteksi kerentanan keamanan statis.
