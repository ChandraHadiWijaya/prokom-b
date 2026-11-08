from pathlib import Path

path = Path(__file__).parent / 'guest.txt'

nama = input("Masukkan nama Anda: ")

path.write_text(nama)

print(f"Terima kasih! Nama '{nama}' telah disimpan di berkas guest.txt.")
