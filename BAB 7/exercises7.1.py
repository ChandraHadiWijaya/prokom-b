#rental

stok_mobil = ['avanza', 'innova', 'fortuner', 'pajero', 'brio',]

# Meminta input jenis mobil dari pengguna
car_request = input("Mobil apa yang ingin Anda sewa? ")

# Mengecek apakah mobil yang diminta ada di dalam stok
if car_request.lower() in stok_mobil:
    print(f"Tunggu sebentar, saya lihat dulu... Ah ada! Mobil {car_request.title()} tersedia dan siap disewa.")
else:
    print(f"Maaf, saat ini mobil {car_request.title()} tidak tersedia di rental kami.")
