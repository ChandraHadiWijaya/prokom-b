#album pengguna

def make_album(artist_name, album_title, number_of_songs=None):
    """Membangun dictionary yang mendeskripsikan album musik."""
    album_dict = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    
    if number_of_songs:
        album_dict['songs'] = number_of_songs
        
    return album_dict

while True:
    print("\n--- Masukkan Informasi Album Musik ---")
    print("(Ketik 'q' kapan saja untuk keluar)")
    
    artis = input("Nama Musisi/Penyanyi: ")
    if artis.lower() == 'q':
        break
        
    judul = input("Judul Album: ")
    if judul.lower() == 'q':
        break
        
    album_user = make_album(artis, judul)
    print(f"\nKamus album yang berhasil dibuat:\n{album_user}")

print("\nTerima kasih telah menggunakan program!")
