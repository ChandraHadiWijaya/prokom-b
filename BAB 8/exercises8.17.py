#merapihkan gaya kode

#Program 1: Modifikasi dari Latihan 8-4 (Kaus Besar)
#Aturan PEP 8 yang diterapkan: Tidak ada spasi di sekitar tanda = untuk default value. Baris kode di dalam fungsi dipotong agar tidak terlalu panjang.
def make_shirt(size='xxl', message='fortiva terbaikk'):
    """Menampilkan ringkasan kaus dengan nilai bawaan."""
    print(f"Membuat kaus ukuran {size.upper()} dengan tulisan sablon: '{message}'.")


make_shirt()

make_shirt(size='m')

make_shirt(size='s', message='uns kerenn!')

#Program 2: Modifikasi dari Latihan 8-7 (Album Musik)
#Aturan PEP 8 yang diterapkan: Menggunakan spasi baris kosong yang konsisten untuk memisahkan logika. Penulisan nama variabel menggunakan snake_case (huruf kecil semua dipisah underscore).
def make_album(artist_name, album_title, number_of_songs=None):
    """Membangun dictionary yang mendeskripsikan album musik."""
    album_dict = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    if number_of_songs:
        album_dict['songs'] = number_of_songs
        
    return album_dict

album1 = make_album('Chrisye ', 'Badai Pasti Berlalu')
album2 = make_album('oasis', '(Whats the Story) Morning Glory?')
album3 = make_album('HIVI!', 'Ceritera')

print(album1)
print(album2)
print(album3)

album_spesial = make_album('The Changcuters', 'Mencoba Sukses Kembali', 15)
print(album_spesial)

#Program 3: Modifikasi dari Latihan 8-14 (Informasi Mobil)
#Aturan PEP 8 yang diterapkan: Mengatur posisi argumen yang panjang di dalam pemanggilan fungsi agar sejajar secara vertikal (hanging indent) sehingga lebih mudah dibaca dan tidak melebihi 79 karakter per baris.
def make_car(manufacturer, model, **car_info):
    """Menyimpan informasi tentang mobil ke dalam dictionary."""
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model
    return car_info


car = make_car(
    'ford', 
    'ranger',
    color='black',
    transmission='manual',
    drive_type='4x4'
    )

print("\n🚗 Data mobil berhasil disimpan:")
print(car)
