import os

def create_and_read_file(filename, content):
    # Menulis ke file
    with open(filename, 'w') as f:
        f.write(content)
    
    # Membaca dari file
    with open(filename, 'r') as f:
        data = f.read()
    return data

if __name__ == "__main__":
    print("=== Sistem Manajemen File ===")
    nama_file = "data_dummy.log"
    pesan = "Ini adalah log otomatis yang dibuat oleh file_manager.py"
    
    hasil = create_and_read_file(nama_file, pesan)
    print(f"File '{nama_file}' berhasil dibuat!")
    print(f"Isi file: {hasil}")