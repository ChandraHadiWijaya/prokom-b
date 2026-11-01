#tempat favorit

favorite_places = {
    'tiara': ['senayan', 'gunung rinjani', 'central park mall'],
    'neejad': ['Kost pelangi'],
    'putri': ['bandung', 'bogor'],
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()} adalah:")
    for place in places:
        print(f"\t- {place.title()}")
