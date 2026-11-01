#pengembangan

cities = {
    'solo': {
        'country': 'indonesia',
        'population': '522 ribu',
        'landmark': 'Keraton Surakarta Hadiningrat',
        'fact': 'Dikenal dengan semboyan "Solo The Spirit of Java".',
    },
    'munich': {
        'country': 'jerman',
        'population': '1.5 juta',
        'landmark': 'Marienplatz & Allianz Arena',
        'fact': 'Kota penyelenggara festival tahunan Oktoberfest.',
    },
    'melbourne': {
        'country': 'australia',
        'population': '5 juta',
        'landmark': 'Flinders Street Railway Station',
        'fact': 'Pusat seni budaya dan kota paling layak huni.',
    }
}

print("=== LAPORAN INFORMASI KOTA DUNIA ===")
for city, info in cities.items():
    print(f"\n📌 KOTA: {city.upper()}")
    print(f"  🏳️  Negara    : {info['country'].title()}")
    print(f"  👥 Populasi  : {info['population']}")
    print(f"  🏛️  Landmark  : {info['landmark']}")
    print(f"  ℹ️  Fakta Unik : {info['fact']}")
print("\n====================================")
