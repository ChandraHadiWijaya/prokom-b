import json
from pathlib import Path

# Menentukan path file JSON aman di folder yang sama
path = Path(__file__).parent / 'favorite_number.json'

angka_favorit = input("Masukkan angka favorit kamu: ")

# json.dumps() mengubah data menjadi format teks JSON
data_json = json.dumps(angka_favorit)
path.write_text(data_json)

print("Angka favorit kamu berhasil disimpan!")
