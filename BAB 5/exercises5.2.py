# Lebih Banyak Tes Bersyarat

print("--- Uji Persamaan & Pertidaksamaan String ---")
mobil = 'ford'
print("Apakah mobil == 'ford'? Prediksi saya: True.")
print(mobil == 'ford')

print("Apakah mobil != 'ford'? Prediksi saya: False.")
print(mobil != 'subaru')

print("--- Uji Metode lower() ---")
nama_pengguna = 'jeon_ara'
print("Apakah nama_pengguna.lower() == 'jeon_ara'? Prediksi saya: True.")
print(nama_pengguna.lower() == 'jeon_ara')

print("Apakah nama_pengguna.lower() == 'jeon_ara'? Prediksi saya: False.")
print(nama_pengguna.lower() == 'jeon_ara')

print("--- Uji Numerik ---")
usia = 21

print("Apakah usia == 21? Prediksi saya: True.")
print(usia == 21)
print("Apakah usia != 21? Prediksi saya: False.")
print(usia != 21)

print("Apakah usia > 18? Prediksi saya: True.")
print(usia > 18)
print("Apakah usia < 15? Prediksi saya: False.")
print(usia < 15)

print("Apakah usia >= 21? Prediksi saya: True.")
print(usia >= 21)
print("Apakah usia <= 20? Prediksi saya: False.")
print(usia <= 20)


print("--- Uji Logika AND / OR ---")
usia_0 = 22
usia_1 = 18

print("Apakah usia_0 > 20 and usia_1 > 16? Prediksi saya: True.")
print(usia_0 > 20 and usia_1 > 16)

print("Apakah usia_0 > 20 and usia_1 > 20? Prediksi saya: False.")
print(usia_0 > 20 and usia_1 > 20)

print("Apakah usia_0 > 30 or usia_1 > 16? Prediksi saya: True.")
print(usia_0 > 30 or usia_1 > 16)

print("Apakah usia_0 > 30 or usia_1 > 30? Prediksi saya: False.")
print(usia_0 > 30 or usia_1 > 30)

print("--- Uji Item di Dalam List ---")
toping_pesanan = ['jamur', 'daging', 'sosis']

print("Apakah 'sosis' ada di dalam toping_pesanan? Prediksi saya: True.")
print('sosis' in toping_pesanan)

print("Apakah 'pepperoni' ada di dalam toping_pesanan? Prediksi saya: False.")
print('pepperoni' in toping_pesanan)

print("--- Uji Item TIDAK di Dalam List ---")
pengguna_diblokir = ['neejad', 'kennard', 'sultan']

print("Apakah 'sulaiman' tidak ada di dalam pengguna_diblokir? Prediksi saya: True.")
print('sulaiman' not in pengguna_diblokir)

print("Apakah 'alif' tidak ada di dalam pengguna_diblokir? Prediksi saya: False.")
print('alif' not in pengguna_diblokir)
