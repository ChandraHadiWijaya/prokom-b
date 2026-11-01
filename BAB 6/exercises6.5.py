#rivers

rivers = {
    'nile': 'mesir',
    'amazon': 'brazil',
    'bengawan solo': 'indonesia',
}

print("--- Informasi Sungai ---")
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melewati {country.title()}.")

print("\n--- Nama-Nama Sungai ---")
for river in rivers.keys():
    print(river.title())

# 3. Loop untuk mencetak nama setiap negara saja
print("\n--- Nama-Nama Negara ---")
for country in rivers.values():
    print(country.title())
