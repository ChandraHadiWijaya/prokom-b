import json
from pathlib import Path

path = Path(__file__).parent / 'favorite_number.json'

try:
    konten = path.read_text()
except FileNotFoundError:
    angka_favorit = input("Masukkan angka favorit kamu: ")
    data_json = json.dumps(angka_favorit)
    path.write_text(data_json)
    print("Terima kasih, angka favorit kamu sudah diingat!")
else:
    angka = json.loads(konten)
    print(f"Aku tahu angka favorit kamu! Angkanya adalah {angka}.")
