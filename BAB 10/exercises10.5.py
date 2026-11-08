from pathlib import Path

path = Path(__file__).parent / 'guest_book.txt'

konten_buku_tamu = ""

print("--- PROGRAM BUKU TAMU ---")
print("(Ketik 'keluar' jika sudah selesai menginput nama)\n")

while True:
    nama = input("Masukkan nama tamu: ")
    if nama.lower() == 'keluar':
        break
    
    konten_buku_tamu += nama + "\n"
    print(f"Halo {nama}, nama Anda telah dicatat di daftar antrean.\n")

path.write_text(konten_buku_tamu)

print("\nSelesai! Seluruh nama di atas telah berhasil disimpan ke dalam guest_book.txt.")
