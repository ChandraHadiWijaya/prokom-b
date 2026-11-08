from random import choice

koleksi_lotere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Memilih 4 item secara acak tanpa duplikat
kombinasi_pemenang = []
print("Sedang mengacak tiket pemenang...")

while len(kombinasi_pemenang) < 4:
    pilihan = choice(koleksi_lotere)
    # Memastikan tidak ada angka/huruf yang kembar terpilih dua kali
    if pilihan not in kombinasi_pemenang:
        kombinasi_pemenang.append(pilihan)

# Mencetak pesan pengumuman tiket pemenang
print(f"Setiap tiket yang cocok dengan 4 angka atau huruf ini: {kombinasi_pemenang} berhak mendapatkan hadiah utama!")
