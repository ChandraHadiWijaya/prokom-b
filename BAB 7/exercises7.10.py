#liburan impian

responses = {}

polling_active = True

while polling_active:

    name = input("\nSiapa nama Anda? ")
    response = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda ingin pergi? ")
    
    responses[name] = response
    
    repeat = input("Apakah ada orang lain yang ingin mengisi polling? (ya / tidak) ")
    if repeat.lower() == 'tidak':
        polling_active = False

print("\n--- HASIL POLLING LIBURAN IMPIAN ---")
for name, place in responses.items():
    print(f"{name.title()} ingin berlibur ke {place.title()}.")
