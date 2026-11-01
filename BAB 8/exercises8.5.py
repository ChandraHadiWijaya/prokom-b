#Kota-Kota

def describe_city(city, country='indonesia'):
    """Menampilkan informasi nama kota dan negaranya."""
    print(f"Kota {city.title()} terletak di negara {country.title()}.")

describe_city('jakarta')

describe_city('solo')

describe_city('munich', 'jerman')
