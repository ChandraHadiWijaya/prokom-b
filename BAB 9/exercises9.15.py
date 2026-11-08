from random import choice

def ambil_tiket_acak(koleksi):
    """Fungsi pembantu untuk membuat kombinasi 4 pilihan acak unik."""
    tiket = []
    while len(tiket) < 4:
        pilihan = choice(koleksi)
        if pilihan not in tiket:
            tiket.append(pilihan)
    return tiket

# Koleksi angka dan huruf yang sama seperti nomor 9-14
koleksi_lotere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Membuat satu kombinasi tiket milik kita sendiri
my_ticket = [7, 3, 'A', 'E']
print(f"Tiket target Anda: {my_ticket}")

# Variabel pembantu untuk menghitung berapa kali loop berjalan
jumlah_percobaan = 0
menang = False

# Loop akan terus berjalan sampai mendapatkan tiket yang sama persis
while not menang:
    kombinasi_terambil = ambil_tiket_acak(koleksi_lotere)
    jumlah_percobaan += 1
    
    # Cek apakah tiket yang diundi sama dengan tiket milik kita
    if kombinasi_terambil == my_ticket:
        menang = True

print(f"Selamat! Tiket Anda menang setelah mesin melakukan pengundian sebanyak: {jumlah_percobaan} kali.")
