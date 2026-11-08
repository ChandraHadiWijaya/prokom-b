def format_city_country(city, country, population=None):
    """Menghasilkan format nama kota dan negara dengan jumlah populasi yang opsional."""
    if population:
        formatted_string = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_string = f"{city.title()}, {country.title()}"
    return formatted_string
