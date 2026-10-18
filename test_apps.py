import platform

def get_system_info():
    return {
        "Sistem Operasi": platform.system(),
        "Versi OS": platform.release(),
        "Arsitektur": platform.machine()
    }

if __name__ == "__main__":
    print("=== Pengecekan Informasi Sistem ===")
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")