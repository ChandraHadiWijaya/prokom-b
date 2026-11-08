import json
from pathlib import Path

path = Path(__file__).parent / 'user_profile.json'

try:
    konten = path.read_text()
except FileNotFoundError:
    print("--- Pendaftaran Profil Baru ---")
    # Meminta tiga informasi data pengguna
    username = input("Masukkan username baru: ")
    hobi = input("Apa hobi kamu: ")
    kota = input("Kamu tinggal di kota mana: ")

    # Menyatukan data ke dalam bentuk Dictionary Python (Materi Bab 6)
    profil_user = {
        'username': username,
        'hobi': hobi,
        'kota': kota
    }

    # Menyimpan dictionary utuh ke berkas JSON
    path.write_text(json.dumps(profil_user))
    print("\nProfil kamu berhasil disimpan!")
else:
    # Membaca kembali teks JSON menjadi bentuk Dictionary Python
    profil = json.loads(konten)
    print("\n--- Data Pengguna yang Diingat Sistem ---")
    print(f"Username: {profil['username']}")
    print(f"Hobi:     {profil['hobi']}")
    print(f"Kota:     {profil['kota']}")
