#album musik

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
