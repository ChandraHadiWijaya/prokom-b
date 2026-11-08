import json
from pathlib import Path

def get_stored_username(path):
    """Mendapatkan username yang tersimpan jika ada."""
    try:
        konten = path.read_text()
    except FileNotFoundError:
        return None
    else:
        return json.loads(konten)

def get_new_username(path):
    """Meminta username baru dan menyimpannya ke berkas."""
    username = input("Masukkan nama kamu: ")
    path.write_text(json.dumps(username))
    return username

def greet_user():
    """Menyapa pengguna dan memverifikasi identitasnya."""
    path = Path(__file__).parent / 'username.json'
    username = get_stored_username(path)

    if username:
        # [BARU DI 10-14]: Melakukan konfirmasi identitas ke pengguna
        tanya = input(f"Apakah kamu adalah {username}? (ya/tidak): ")
        if tanya.lower() == 'ya':
            print(f"Selamat datang kembali, {username}!")
        else:
            # Jika bukan, panggil fungsi untuk membuat username baru
            print("\nOalah, mari kita daftarkan pengguna baru.")
            username = get_new_username(path)
            print(f"Kami akan mengingat kamu saat kembali nanti, {username}!")
    else:
        # Kondisi jika program baru pertama kali dijalankan (file belum ada)
        username = get_new_username(path)
        print(f"Kami akan mengingat kamu saat kembali nanti, {username}!")

# Menjalankan fungsi utama program
greet_user()
