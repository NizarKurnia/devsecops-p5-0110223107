def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * hitung_faktorial(n-1)

if __name__ == "__main__":
    print("=== Kalkulator Faktorial ===")
    angka = 5
    hasil = hitung_faktorial(angka)
    print(f"Faktorial dari {angka} adalah {hasil}")