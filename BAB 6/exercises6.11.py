#kota kota

cities = {
    'solo': {
        'country': 'indonesia',
        'population': '522 ribu',
        'fact': 'Dikenal sebagai salah satu pusat kebudayaan Jawa yang kental dengan semboyan "Solo The Spirit of Java".',
    },
    'munich': {
        'country': 'jerman',
        'population': '1.5 juta',
        'fact': 'Terkenal di seluruh dunia sebagai kota penyelenggara festival tahunan Oktoberfest.',
    },
    'melbourne': {
        'country': 'australia',
        'population': '5 juta',
        'fact': 'Sering dinobatkan sebagai salah satu kota paling layak huni di dunia dan pusat seni budaya Australia.',
    }
}

for city, city_info in cities.items():
    print(f"\nKota: {city.title()}")
    print(f"\tNegara: {city_info['country'].title()}")
    print(f"\tPopulasi: {city_info['population']}")
    print(f"\tFakta: {city_info['fact']}")
