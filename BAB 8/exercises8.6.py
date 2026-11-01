#nama kota

def city_country(city, country):
    """Mengembalikan string nama kota dan negara yang diformat rapi."""
    return f"{city.title()}, {country.title()}"

print(city_country('santiago', 'chile'))
print(city_country('solo', 'indonesia'))
print(city_country('tokyo', 'jepang'))
