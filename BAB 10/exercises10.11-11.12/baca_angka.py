import json
from pathlib import Path

path = Path(__file__).parent / 'favorite_number.json'

try:
    # Mencoba membaca berkas teks JSON
    konten = path.read_text()
    # json.loads() mengubah kembali teks JSON menjadi data Python
    angka = json.loads(konten)
except FileNotFoundError:
    print("Kamu belum menyimpan angka favorit!")
else:
    print(f"Aku tahu angka favorit kamu! Angkanya adalah {angka}.")
